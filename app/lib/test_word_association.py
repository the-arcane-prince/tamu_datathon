# import pytest
from . import word_association as wa
from .training_data.load_data import load_all_data
import json

def test_sample():
    print("Hello World")

async def test_word_association():
    
    bigarr = []
    with open('data.json', 'r') as file:
        data = json.load(file)
        

        
        num = 3
        for x in range (num):
            words = []
            for entry in data[x]:
                words.extend(entry['words'])
            bigarr.append(words)
    print(bigarr)
    for arr in bigarr:
        x = wa.WordAssociations()
        ans = await x.compute_word_associations(arr)
        x.print_word_association_matrix(ans)

        
#     ans = await x.get_similarity_rankings([
#     "BLUES", "COUNTRY", "FOLK", "ROCK",  # Music genres
#     "BIRDS", "NOTORIOUS", "REBECCA", "ROPE",  # Famous movie titles
#     "BAR", "FINAL", "ORAL", "PHYSICAL",  # Types of exams
#     "KISS", "NERD", "RUNT", "WHOPPER"  # Candy pieces
# ])
#    print(ans)
