import unittest
from src.logic import render_masked_word, is_win, validate_guess

class TestLogic(unittest.TestCase):

    def test_render_masked_word(self):
        self.assertEqual(render_masked_word("apple", set()), "_ _ _ _ _")
        self.assertEqual(render_masked_word("apple", {"a", "p"}), "a p p _ _")

    def test_is_win(self):
        self.assertTrue(is_win("apple", {"a", "p", "l", "e"}))
        self.assertFalse(is_win("apple", {"a", "p"}))

    def test_validate_guess(self):
        guessed = set("a")
        valid, msg = validate_guess("b", guessed)
        self.assertTrue(valid)

        valid, msg = validate_guess("a", guessed)
        self.assertFalse(valid)

        valid, msg = validate_guess("1", guessed)
        self.assertFalse(valid)

        valid, msg = validate_guess("ab", guessed)
        self.assertFalse(valid)

if __name__ == "__main__":
    unittest.main()
