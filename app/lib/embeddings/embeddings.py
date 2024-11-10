class EmbeddingsModel:
    def __init__(self, embedding_model) -> None:
        self.embedding_model = embedding_model
        
    def embed(self, text: str) -> str:
        return self.embedding_model.encode(text, task="text-matching")
        
    def embed_many(self, texts: list[str]) -> list[str]:
        return self.embedding_model.encode(texts, task="text-matching")
    
    def dimensions(self) -> int:
        return self.embedding_model.config.hidden_size
    
    def model_name(self) -> str:
        return self.embedding_model.config.model