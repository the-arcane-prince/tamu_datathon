import polars as pl
from sklearn.metrics.pairwise import cosine_similarity
from .embeddings.embeddings import EmbeddingsModel
from .embeddings.remote_embed import RemoteEmbeddingsModel
from itertools import combinations
class WordAssociations:
    
    """
    Create and initialize the model and 
    """
    def __init__(self):
        self.model = EmbeddingsModel(RemoteEmbeddingsModel("clustering", "models/embedding-001"))
        self.vector = []


    """
    A list ranking words by their average similarity to the other words
    """    
    async def get_similarity_rankings(self, words: list[str]) -> list[str]:
        print(words)
        if not self.vector:
            temp  = await self.model.embed_many(words)
            self.vector = temp['embedding']
        similarity_matrix = cosine_similarity(self.vector)
        avg_similarities = similarity_matrix.mean(axis=1)

        ranked_words = [word for _, word in sorted(zip(avg_similarities, words), reverse=True)]
        print(ranked_words)
        return ranked_words
    
    """
    A four element list of the most similar words in the dataset
    """
    async def get_most_similar_words(self, words: list[str], top_x : int) -> list[str]:
        if not self.vector:
            temp  = await self.model.embed_many(words)
            self.vector = temp['embedding']
        similarity_df = await self.compute_word_associations(words)
        
        # Convert the Polars DataFrame to a numpy array for easier access
        similarity_matrix = similarity_df.to_numpy()

        # List to store all possible word groups
        similarity_groups = []

        # Step 2: Find the top 4 similar words for each word and form groups
        for i, word in enumerate(words):
            similarities = similarity_matrix[i]
            similarities[i] = -100  # Exclude the word's similarity to itself
            
            # Get the indices of the top 4 most similar words
            most_similar_indices = similarities.argsort()[-4:][::-1]
            similar_words = [words[idx] for idx in most_similar_indices]
            
            # Add the group (set of 4 similar words) to the list
            similarity_groups.append(similar_words)

        # Step 3: Score the groups based on total pairwise similarities
        group_scores = []
        for group in similarity_groups:
            score = 0
            for word1, word2 in combinations(group, 2):  # Calculate pairwise similarity within the group
                idx1 = words.index(word1)
                idx2 = words.index(word2)
                score += similarity_matrix[idx1, idx2]
            group_scores.append((group, score))

        # Step 4: Sort groups by their total similarity score in descending order
        group_scores.sort(key=lambda x: x[1], reverse=True)


        return [group for group, score in group_scores[:top_x]]
        
    
    """
    Given a list of words create a matrix that gives the similarity
    score between two words
    """
    async def compute_word_associations(self, words: list[str]) -> pl.DataFrame:
        if not self.vector:
            temp  = await self.model.embed_many(words)
            self.vector = temp['embedding']
        similarity_matrix = cosine_similarity(self.vector)
        # Convert the numpy similarity matrix into a Polars DataFrame
        # Convert the matrix into a list of lists and use the words as both row and column labels

        # Convert the numpy similarity matrix into a Polars DataFrame
        similarity_df = pl.DataFrame(similarity_matrix.tolist())

        # Set the column names directly by using words as column names
        similarity_df.columns = [str(word) for word in words]  # Set column names as strings
        similarity_df.rows = [str(word) for word in words]
        # Optionally, you can also rename the rows, if necessary, by using the same word list

        return similarity_df
    
    """
    Print the similarity matrix
    """
    def print_word_association_matrix(self, df: pl.DataFrame) -> None:
        
        print(df)