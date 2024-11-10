class EmbeddingsModel:
    def __init__(self, embedding_model) -> None:
        self.embedding_model = embedding_model
        
    def embed(self, text: str) -> str:
        return self.embedding_model.embed(text)
        
    def embed_many(self, texts: list[str]) -> list[str]:
        return self.embedding_model.embed_many(texts)
    
    def dimensions(self) -> int:
        return self.embedding_model.config.hidden_size
    
    def model_name(self) -> str:
        return self.embedding_model.config.model