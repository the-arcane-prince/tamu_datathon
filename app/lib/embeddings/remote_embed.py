import os
import google.generativeai as gemini

from dotenv import load_dotenv




"""
Make sure that there is an Api Key in the enviornment
variables called GEMINI_API_KEY
"""
class RemoteEmbeddingsModel:
    
    def __init__(self, task_type: str, model_name: str):
        load_dotenv()
        gemini.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.task_type = task_type
        self.model = model_name
    
    def embed(self, text: str):
        return gemini.embed_content_async(
            task_type=self.task_type,
            model=self.model,
            content=text
        )
    
    def embed_many(self, texts: list[str]):
        return gemini.embed_content_async(
            task_type=self.task_type,
            model=self.model,
            content=texts
        )
    
    def dimensions(self):
        print("Dimensions not available for remote embeddings")
    
    def model_name(self):
        return self.model