# Save the Watermelon — Test Plan

## Test Matrix

| Feature | Test Case | Expected Result |
|---------|-----------|----------------|
| Word selection | select_secret_word returns a word from WORDS | Always returns a string from the word list |
| Masked word | render_masked_word with no guesses | All underscores matching word length |
| Masked word | render_masked_word with some guesses | Correct letters revealed, others underscores |
| Win check | is_win with all letters guessed | Returns True |
| Win check | is_win with missing letters | Returns False |
| Input validation | Single valid letter | Returns True |
| Input validation | More than one letter | Returns False, error message |
| Input validation | Non-alphabet | Returns False, error message |
| Input validation | Already guessed letter | Returns False, error message |
| Game loop | Player guesses correctly until word complete | Win message displayed |
| Game loop | Player runs out of slices | Lose message displayed |
| Replay | Player chooses "y" | Game restarts |
| Replay | Player chooses "n" | Game ends |

---

## Manual Test Transcript / Notes

### Test 1 — Correct guesses
- Secret word: `apple`
- Guesses: `a`, `p`, `l`, `e`
- Result: Win message displayed, slices remaining ≥ 0

### Test 2 — Incorrect guesses
- Secret word: `kiwi`
- Guesses: `a`, `b`, `c`, `d`, `e`, `f`
- Result: Lose message displayed, slices = 0

### Test 3 — Invalid inputs
- Guesses: `aa`, `1`, `@`, `a` (repeated)
- Result: Error messages displayed, no slice deducted for invalid/repeat guesses

### Test 4 — Replay
- After win/lose, choose "y" → game restarts
- After win/lose, choose "n" → game ends

---

## Known Issues / Limitations
- No difficulty levels implemented
- Word list is small
- No ASCII art or categories
