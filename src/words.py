import random

# Word list — can also be loaded from data/words.txt
WORDS = [
    "watermelon", "apple", "banana", "orange", "grape", "strawberry",
    "melon", "kiwi", "peach", "mango"
]

def select_secret_word():
    """Return a random word from the word list."""
    return random.choice(WORDS)
