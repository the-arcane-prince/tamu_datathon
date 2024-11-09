import pytest
import word_association as wa

def test_sample():
    print("Hello World")

def test_word_association():
    x = wa.WordAssociations()
    e = x.compute_embeddings("Hello")
    print(e)