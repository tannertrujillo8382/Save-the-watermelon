# src/words.py
import random

WORD_LIST = [
    "watermelon",
    "apple",
    "banana",
    "grape",
    "orange",
    "mango",
]

def choose_word():
    """Return a random word from the list"""
    return random.choice(WORD_LIST)
