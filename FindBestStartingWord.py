from collections import Counter
import itertools
import math
from Wordle import Wordle


class FindBestStartingWord:
    def __init__(self, wordle_game):
        self.wordle_game = wordle_game

    def generate_all_feedbacks(self):
        symbols = ['G', 'Y', '_']
        return [''.join(p) for p in itertools.product(symbols, repeat=5)]

    def calculate_entropy(self, guess):
        feedback_counts = Counter()
        for target in self.wordle_game.answers:
            feedback = self.wordle_game.get_feedback(guess, target)
            feedback_counts[feedback] += 1
        total = sum(feedback_counts.values())
        entropy = 0.0
        for count in feedback_counts.values():
            probability = count / total
            entropy -= probability * math.log2(probability)
        return entropy

    def find_best_starting_word(self):
        best_guess = None
        highest_entropy = -1
        total_words = len(self.wordle_game.allowed_guesses)
        for i, guess in enumerate(self.wordle_game.allowed_guesses):
            entropy = self.calculate_entropy(guess)
            if entropy > highest_entropy:
                highest_entropy = entropy
                best_guess = guess
        return best_guess
    
answers_file = 'answers.txt'
allowed_guesses_file = 'allowed_guesses.txt'

game = Wordle(answers_file, allowed_guesses_file)
best_first_guess = FindBestStartingWord(game).find_best_starting_word()
print(best_first_guess)