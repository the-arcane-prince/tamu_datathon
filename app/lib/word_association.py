import polars as pl
from sklearn.metrics.pairwise import cosine_similarity
from .embeddings.embeddings import EmbeddingsModel
from .embeddings.remote_embed import RemoteEmbeddingsModel

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
        print(self.vector)
        similarity_matrix = cosine_similarity(self.vector)
        print(similarity_matrix)
        avg_similarities = similarity_matrix.mean(axis=1)

        ranked_words = [word for _, word in sorted(zip(avg_similarities, words), reverse=True)]
        print(ranked_words)
        return ranked_words
    
    """
    A four element list of the most similar words in the dataset
    """
    def get_most_similar_words(self, words: list[str]) -> list[str]:
        if(self.vector==[]):
            self.vector = self.model.embed_many(words)
        pass
    
    """
    Given a list of words create a matrix that gives the similarity
    score between two words
    """
    def compute_word_associations(self, words: list[str]) -> pl.DataFrame:
        if self.vector == []:
            self.vector = self.model.embed_many(words)
    
    """
    Print the similarity matrix
    """
    def print_word_association_matrix(self, df: pl.DataFrame) -> None:
        
        print(df)