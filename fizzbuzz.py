class Fizzbuzz(object):
  def play(self, number):
    if number%3 == 0:
      return 'fizz'
    elif number%5 == 0:
      return 'buzz'
