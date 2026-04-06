def render_masked_word(secret_word, guessed_letters):
    """Return the word with guessed letters revealed, others as underscores."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

def is_win(secret_word, guessed_letters):
    """Check if all letters in the secret word have been guessed."""
    return all(letter in guessed_letters for letter in secret_word)

def validate_guess(guess, guessed_letters):
    """Return True if guess is a valid, single, new letter; otherwise False."""
    if len(guess) != 1:
        return False, "Please enter a single letter."
    if not guess.isalpha():
        return False, "Please enter a letter (a-z)."
    if guess.lower() in guessed_letters:
        return False, "You already guessed that letter."
    return True, ""
