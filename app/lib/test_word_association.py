# import pytest
from . import word_association as wa
from .training_data.load_data import load_all_data

def test_sample():
    print("Hello World")

async def test_word_association():
    x = wa.WordAssociations()
    ans = await x.get_similarity_rankings([
    "BLUES", "COUNTRY", "FOLK", "ROCK",  # Music genres
    "BIRDS", "NOTORIOUS", "REBECCA", "ROPE",  # Famous movie titles
    "BAR", "FINAL", "ORAL", "PHYSICAL",  # Types of exams
    "KISS", "NERD", "RUNT", "WHOPPER"  # Candy pieces
])
    print(ans)
