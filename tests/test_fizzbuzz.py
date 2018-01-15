import unittest
from fizzbuzz import Fizzbuzz

class FizzbuzzTest(unittest.TestCase):
  def test_returns_fizz_with_value_3(self):
    game = Fizzbuzz()
    result = game.play(3)
    self.assertEqual('fizz', result)

  def test_returns_fizz_with_value_9(self):
    game = Fizzbuzz()
    result = game.play(9)
    self.assertEqual('fizz', result)

  def test_returns_fizz_with_value_5(self):
    game = Fizzbuzz()
    result = game.play(5)
    self.assertEqual('buzz', result)

  def test_returns_fizz_with_value_10(self):
    game = Fizzbuzz()
    result = game.play(10)
    self.assertEqual('buzz', result)

  def test_returns_fizz_with_value_15(self):
    game = Fizzbuzz()
    result = game.play(15)
    self.assertEqual('fizzbuzz', result)
