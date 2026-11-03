import contextlib
import io
import runpy
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]

def play(filename, answers, random_value=0):
    output = io.StringIO()
    with patch("builtins.input", side_effect=answers), patch("random.randint", return_value=random_value), contextlib.redirect_stdout(output):
        try:
            runpy.run_path(str(ROOT / filename), run_name="__main__")
        except SystemExit:
            pass
    return output.getvalue()

class GameTests(unittest.TestCase):
    def test_guesser_hints_and_attempt_count(self):
        result = play("number_guesser.py", ["10", "9", "2", "5"], 5)
        self.assertIn("above the number", result)
        self.assertIn("below the number", result)
        self.assertIn("3 guesses", result)

    def test_quiz_score(self):
        result = play("quiz_game.py", ["yes", "central processing unit", "wrong", "random access memory", "wrong"])
        self.assertIn("2 questions correct", result)
        self.assertIn("50.0% correct", result)

    def test_tie_does_not_count_as_loss(self):
        result = play("rock_paper_scissors.py", ["rock", "q"], 0)
        self.assertIn("tie", result.lower())
        self.assertIn("You won 0 times", result)
        self.assertIn("computer won 0 times", result)

    def test_winning_and_losing_rounds(self):
        result = play("rock_paper_scissors.py", ["paper", "scissors", "q"], 0)
        self.assertIn("You won 1 times", result)
        self.assertIn("computer won 1 times", result)

if __name__ == "__main__":
    unittest.main()
