import polars as pl
from .embeddings.embeddings import EmbeddingsModel
from .embeddings.remote_embed import RemoteEmbeddingsModel

class WordAssociations:
    
    """
    Create and initialize the model and 
    """
    def __init__(self):
        self.model = EmbeddingsModel(RemoteEmbeddingsModel("clustering", "models/embedding-001"))

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