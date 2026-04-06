# Save the Watermelon — Design Document

## Problem Statement & Target Audience
The goal of this game is to save the watermelon by guessing letters before the "slice counter" runs out.  
The target audience is beginner Python players or casual gamers who enjoy word-guessing challenges.

## Game Rules
- A secret word is randomly chosen from a list.
- The word is displayed with underscores for unguessed letters.
- The player guesses one letter at a time.
- Correct guesses reveal the letters in the word.
- Incorrect guesses reduce the "slice counter" (lives).
- The game ends when the player either:
  - Reveals all letters → WIN
  - Slice counter reaches 0 → LOSE

## Core Features (Must-Have)
- Random word selection
- Display of masked word
- Letter-by-letter input
- Slice counter and win/lose detection
- Input validation (single letters, alphabet only, no repeats)

## Stretch Goals (Nice-to-Have)
- ASCII art watermelon stages
- Difficulty levels
- Word categories
- Scoreboard for multiple rounds

## Basic Flow (Bullet)
1. Start game
2. Pick a random word
3. Initialize guessed letters set and slice counter
4. Loop:
   - Display masked word
   - Prompt for a letter
   - Check input validity
   - Update guessed letters and slices
5. Check for win or lose
6. Offer replay

## Data Design
- `secret_word` → string
- `guessed_letters` → set of letters guessed
- `remaining_slices` → integer
- `revealed_word` → string with guessed letters and underscores

## Module / Function Responsibilities
- `src/words.py` → Word list and loader
- `src/logic.py` → Core functions (render word, check win, validate input)
- `src/game.py` → Main loop, input/output, runs the game
