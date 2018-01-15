import unittest
from fizzbuzz import Fizzbuzz

class FizzbuzzTest(unittest.TestCase):
  def test_returns_fizz_with_value_3(self):
    game = Fizzbuzz()
    result = game.play(3)

    self.assertEqual('fizz', result)
