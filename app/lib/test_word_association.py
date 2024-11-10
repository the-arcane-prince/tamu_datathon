# import pytest
from . import word_association as wa
from .training_data.load_data import load_all_data
import json

def test_sample():
    print("Hello World")

async def test_word_association():
    num = 20
    bigarr = []
    rightans = []
    with open('data.json', 'r') as file:
        data = json.load(file)
        

        
        
        for x in range (num):
            words = []
            for entry in data[x]:
                words.extend(entry['words'])
            bigarr.append(words)
    with open('data_yellow.json',"r") as file:
        data = json.load(file)
        for x in range (num):
            rightans.append(data[x]["words"])
    print(bigarr)
    for x in range(num):
        arr = bigarr[x]
        print("Correct answer:")
        print(rightans[x])
        x = wa.WordAssociations()

        ans = await x.get_most_similar_words(arr,5)
        print("Top 5 guesses")
        for i in ans:
            print(i)
        
#     ans = await x.get_similarity_rankings([
#     "BLUES", "COUNTRY", "FOLK", "ROCK",  # Music genres
#     "BIRDS", "NOTORIOUS", "REBECCA", "ROPE",  # Famous movie titles
#     "BAR", "FINAL", "ORAL", "PHYSICAL",  # Types of exams
#     "KISS", "NERD", "RUNT", "WHOPPER"  # Candy pieces
# ])
#    print(ans)
