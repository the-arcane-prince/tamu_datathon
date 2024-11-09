import polars as pl
from transformers import AutoModel

class WordAssociations:
    
    """
    Create and initialize the model and 
    """
    def __init__(self):
        self.model = AutoModel.from_pretrained("jinaai/jina-embeddings-v3", trust_remote_code=True)
    
    """
    Generate an embedding for the following word and print the vector result
    """
    def compute_embeddings(self, word: str) -> str:
        return self.model.encode(word, task="text-matching")

    """
    A list ranking words by their average similarity to the other words
    """    
    def get_similarity_rankings(self, words: list[str]) -> list[str]:
        pass
    
    """
    A four element list of the most similar words in the dataset
    """
    def get_most_similar_words(self, words: list[str]) -> list[str]:
        pass
    
    """
    Given a list of words create a matrix that gives the similarity
    score between two words
    """
    def compute_word_associations(self, words: list[str]) -> pl.DataFrame:
        pass
    
    """
    Print the similarity matrix
    """
    def print_word_association_matrix(self, df: pl.DataFrame) -> None:
        print(df)
        