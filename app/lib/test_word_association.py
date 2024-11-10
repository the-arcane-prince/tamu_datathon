# import pytest
from . import word_association as wa
from .training_data.load_data import load_all_data
import json

import polars as pl

import pytest

# def test_sample():
#     print("Hello World")

@pytest.mark.asyncio
async def test_word_association():
    num = 20
    bigarr = []
    rightans = []
    with open('/home/neilshirsatmain/ai/tamu_datathon/data.json', 'r') as file:
        data = json.load(file)
        for x in range (num):
            words = []
            for entry in data[x]:
                words.extend(entry['words'])
            bigarr.append(words)
    with open('/home/neilshirsatmain/ai/tamu_datathon/data_green.json',"r") as file:
        data = json.load(file)
        for x in range (num):
            rightans.append(data[x]["words"])
    print(bigarr)
    for x in range(num):
        arr = bigarr[x]
        print("Correct answer:")
        print(rightans[x])
        x = wa.WordAssociations()
        
        pl.Config.set_tbl_rows(-1)
        pl.Config.set_tbl_cols(-1)
        pl.Config.set_fmt_str_lengths(900)
        pl.Config.set_tbl_width_chars(900)

        print(await x.compute_word_associations(arr))
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
