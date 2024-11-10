import os
import google.generativeai as gemini

"""
Make sure that there is an Api Key in the enviornment
variables called GEMINI_API_KEY
"""
class RemoteEmbeddingsModel:
    
    def __init__(self, task_type: str, model_name: str):
        gemini.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.task_type = task_type
        self.model_name = model_name
    
    def embed(self, text: str):
        return gemini.embed_content_async(
            task_type=self.task_type,
            model_name=self.model_name,
            content=text
        )
    
    def embed_many(self, texts: list[str]):
        return gemini.embed_content_async(
            task_type=self.task_type,
            model_name=self.model_name,
            content=texts
        )
    
    def dimensions(self):
        print("Dimensions not available for remote embeddings")
    
    def model_name(self):
        return self.model_name