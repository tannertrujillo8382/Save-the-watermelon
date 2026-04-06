# src/game.py

"""
Save the Watermelon - Main game loop

This is the entry point for the word-guessing game.
Run from the project root with:
    py -m src.game
"""

from .logic import render_masked_word, is_win, validate_guess
from .words import WORD_LIST, choose_word

MAX_SLICES = 6  # Number of lives per game


def prompt_for_letter(guessed_letters):
    """
    Prompt the player to guess a letter. Validate input:
    - Single character
    - Alphabetic
    - Not already guessed
    """
    while True:
        guess = input("Guess a letter: ").lower()
        valid, message = validate_guess(guess, guessed_letters)
        if valid:
            return guess
        print(message)


def prompt_play_again():
    """
    Ask the player if they want to play again.
    Returns True if 'y', False otherwise.
    """
    response = input("Play again? (y/n): ").strip().lower()
    return response == "y"


def main_game_loop():
    """
    Main loop for a single game session.
    Handles word selection, guesses, and win/loss logic.
    """
    secret_word = choose_word()  # Randomly select a word
    guessed_letters = set()
    remaining_slices = MAX_SLICES

    print("\nWelcome to Save the Watermelon!\n")

    while remaining_slices > 0 and not is_win(secret_word, guessed_letters):
        print("\nWord:", render_masked_word(secret_word, guessed_letters))
        print("Slices remaining:", remaining_slices)

        guess = prompt_for_letter(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print("Nice guess!")
        else:
            remaining_slices -= 1
            print(f"Oops! Slice lost. Remaining slices: {remaining_slices}")

    # End of game
    if is_win(secret_word, guessed_letters):
        print(f"\nYou saved the watermelon! The word was '{secret_word}'.")
    else:
        print(f"\nOh no! The watermelon was sliced. The word was '{secret_word}'.")

    # Prompt to play again
    if prompt_play_again():
        main_game_loop()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main_game_loop()
        print("Thanks for playing!")

if __name__ == "__main__":
    main_game_loop()
