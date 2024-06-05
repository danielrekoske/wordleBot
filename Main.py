from Wordle import Wordle
from WordleBot import WordleBot
from Testing import Testing

answers_file = 'answers.txt'
allowed_guesses_file = 'allowed_guesses.txt'

game = Wordle(answers_file, allowed_guesses_file)

tester = Testing(game)
tester.test_bot()