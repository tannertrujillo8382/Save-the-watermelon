from .logic import render_masked_word, is_win, validate_guess
from .words import WORD_LIST, choose_word
from words import select_secret_word

MAX_SLICES = 6  # Number of lives

def prompt_for_letter(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        valid, message = validate_guess(guess, guessed_letters)
        if valid:
            return guess
        print(message)

def prompt_play_again():
    response = input("Play again? (y/n): ").lower()
    return response == "y"

def main_game_loop():
    secret_word = select_secret_word()
    guessed_letters = set()
    remaining_slices = MAX_SLICES

    print("\nWelcome to Save the Watermelon!\n")

    while remaining_slices > 0 and not is_win(secret_word, guessed_letters):
        print("\nWord: ", render_masked_word(secret_word, guessed_letters))
        print("Slices remaining:", remaining_slices)

        guess = prompt_for_letter(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print("Nice guess!")
        else:
            remaining_slices -= 1
            print(f"Oops! Slice lost. Remaining slices: {remaining_slices}")

    if is_win(secret_word, guessed_letters):
        print(f"\nYou saved the watermelon! The word was '{secret_word}'.")
    else:
        print(f"\nOh no! The watermelon was sliced. The word was '{secret_word}'.")

    if prompt_play_again():
        main_game_loop()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main_game_loop()
