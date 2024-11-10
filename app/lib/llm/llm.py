import llama_cpp as llama
import os

"""
A basic large language model that can be used for the purpose
of querying relational data from natural language

BASE MODEL: LLAMA 3.1 70B; 128K Context Window

TODO: Move the inference to a separate process so the inference
does not block the main process
    - Make the external process contain the chat history for the
      conversation and include a clear history switch in order to
      reset the conversation buffer
"""
class LLM:
    
    """
    Create, intialize, and load the model for inferencing
    """
    def __init__(self):
        self.model = llama.Llama.from_pretrained(
	        repo_id="neil-shirsat/Llama-3.1-8B-Q8_0-GGUF",
	        filename="llama-3.1-8b-q8_0.gguf",
        )
        
    """
    Create a llm request to the llm
    """
    def generate_text(self, prompt):
        return self.model(
            prompt=prompt,
            max_tokens=128000,
            stop=["Q:"],
            echo=False
        )
        
    """
    Create a chat completion to the external llm
    """
    def generate_chat_completion(self, prompt):
        return self.model.generate(
            prompt=prompt,
            max_tokens=128000,
            stop=["Q:"],
            echo=False
        )