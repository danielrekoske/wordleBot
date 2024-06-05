from collections import Counter
import math

class WordleBot:
    def __init__(self, wordle_game):
        self.wordle_game = wordle_game
        self.possible_words = wordle_game.answers[:]
        self.attempts = 6
        self.best_starting_word = "soare"

    def filter_possible_words(self, guess, feedback):
        self.possible_words = [word for word in self.possible_words if self.wordle_game.get_feedback(guess, word) == feedback]

    def make_guess(self, previous_guesses):
        if not previous_guesses:
            return self.best_starting_word

        num_possible_answers = len(self.possible_words)
        best_guess = None
        highest_score = -1

        for guess in self.wordle_game.allowed_guesses:
            entropy = self.calculate_entropy(guess)
            probability_correct = 1 / num_possible_answers if guess in self.possible_words else 0
            score = entropy + probability_correct

            if score > highest_score:
                highest_score = score
                best_guess = guess

        return best_guess

    def calculate_entropy(self, guess):
        feedback_counts = Counter(self.wordle_game.get_feedback(guess, target) for target in self.possible_words)
        total = sum(feedback_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in feedback_counts.values() if count > 0)
        return entropy

    def play(self):
        previous_guesses = []
        for attempt in range(1, self.attempts + 1):
            guess = self.make_guess(previous_guesses)
            feedback = self.wordle_game.get_feedback(guess, self.wordle_game.target_word)
            previous_guesses.append(guess)
            if guess == self.wordle_game.target_word:
                return attempt
            self.filter_possible_words(guess, feedback)
        return self.attempts + 1