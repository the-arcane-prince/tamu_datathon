from transformers import AutoModel

class LocalEmbeddingsModel:
    
    def __init__(self) -> None:
        self.model = AutoModel.from_pretrained("jinaai/jina-embeddings-v3", trust_remote_code=True)
        
    def embed(self, text: str):
        return self.model.encode(text, task="text-matching")
    
    def embed_many(self, texts: list[str]):
        return self.model.encode(texts, task="text-matching")
    
    def dimensions(self):
        return self.model.config.hidden_size
    
    def model_name(self):
        return self.model.config.model