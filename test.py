# tests/test_guess_number.py
import unittest
from guess_number.main import check_guess

class TestGuessNumber(unittest.TestCase):
    def test_correct_guess(self):
        # Simulate correct guess
        result = check_guess(5, 5)
        self.assertEqual(result, True)

    def test_incorrect_guess(self):
        # Simulate incorrect guess
        result = check_guess(3, 5)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
