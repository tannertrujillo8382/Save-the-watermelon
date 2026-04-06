## Main Game Loop

FUNCTION main_game_loop
    secret_word ← select_secret_word()
    guessed_letters ← empty set
    remaining_slices ← MAX_SLICES

    WHILE remaining_slices > 0 AND NOT is_win(secret_word, guessed_letters)
        DISPLAY render_masked_word(secret_word, guessed_letters)
        guess ← prompt_for_letter()

        IF guess IN guessed_letters THEN
            DISPLAY "You already guessed that letter!"
            CONTINUE
        ENDIF

        ADD guess TO guessed_letters

        IF guess IN secret_word THEN
            DISPLAY "Nice guess!"
        ELSE
            remaining_slices ← remaining_slices - 1
            DISPLAY "Slice lost! Remaining slices: " + remaining_slices
        ENDIF
    ENDWHILE

    IF is_win(secret_word, guessed_letters) THEN
        DISPLAY "You saved the watermelon!"
    ELSE
        DISPLAY "Oh no! The watermelon was sliced!"
    ENDIF

    replay ← prompt_play_again()
    IF replay THEN
        main_game_loop()
    ENDIF
END FUNCTION

## Supporting Functions

FUNCTION select_secret_word
    RETURN random word from word list
END FUNCTION

FUNCTION render_masked_word(secret_word, guessed_letters)
    FOR each letter IN secret_word
        IF letter IN guessed_letters THEN
            DISPLAY letter
        ELSE
            DISPLAY "_"
        ENDIF
    ENDFOR
END FUNCTION

FUNCTION is_win(secret_word, guessed_letters)
    RETURN True IF all letters in secret_word are in guessed_letters
    ELSE False
END FUNCTION

FUNCTION prompt_for_letter
    PROMPT "Guess a letter: "
    VALIDATE single alphabetic character
    RETURN valid letter
END FUNCTION

FUNCTION prompt_play_again
    PROMPT "Play again? (y/n): "
    RETURN True IF input is "y", ELSE False
END FUNCTION
