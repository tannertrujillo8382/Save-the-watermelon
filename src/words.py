# src/words.py

import random

# List of words for the game
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
