import random

class Wordle:
    def __init__(self, answers_file, allowed_guesses_file):
        self.answers = self.load_words(answers_file)
        self.allowed_guesses = self.load_words(allowed_guesses_file)
        self.target_word = self.choose_word()
        self.attempts = 6

    def load_words(self, file_name):
        with open(file_name, 'r') as file:
            words = [line.strip() for line in file.readlines()]
        return words

    def choose_word(self):
        return random.choice(self.answers)

    def get_feedback(self, guess, target):
        feedback = ["_" for _ in range(len(target))]
        target_letters = list(target)
        for i in range(len(guess)):
            if guess[i] == target[i]:
                feedback[i] = "G" 
                target_letters[i] = None
        for i in range(len(guess)):
            if feedback[i] == "_" and guess[i] in target_letters:
                feedback[i] = "Y" 
                target_letters[target_letters.index(guess[i])] = None
        return "".join(feedback)

    def play(self):
        print("Welcome to Wordle! Guess the five-letter word.")
        
        for _ in range(self.attempts):
            guess = input("Enter your guess: ").lower()
            if len(guess) != 5:
                print("Please enter a five-letter word.")
                continue
            if guess not in self.allowed_guesses:
                print("Invalid guess. Try again.")
                continue
            feedback = self.get_feedback(guess, self.target_word)
            print(f"Feedback: {feedback}")
            if guess == self.target_word:
                print("Congratulations! You've guessed the word correctly.")
                return
        print(f"Sorry, you've run out of attempts. The word was: {self.target_word}")
