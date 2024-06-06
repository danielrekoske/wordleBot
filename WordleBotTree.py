from collections import Counter

class WordleBotTree:
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
        
        root = TreeNode(self.possible_words, [])
        best_guess = self.search_tree(root, 0)
        return best_guess

    def search_tree(self, node, depth):
        if depth == self.attempts or len(node.possible_words) == 1:
            return node.possible_words[0]
        
        best_guess = None
        best_score = float('inf')

        for guess in self.wordle_game.allowed_guesses:
            feedback_counts = Counter(self.wordle_game.get_feedback(guess, word) for word in node.possible_words)
            branches = [TreeNode([word for word in node.possible_words if self.wordle_game.get_feedback(guess, word) == feedback], node.guesses + [guess]) for feedback in feedback_counts]
            score = sum(len(branch.possible_words)**2 for branch in branches)

            if score < best_score:
                best_score = score
                best_guess = guess

        return best_guess

    def play(self):
        previous_guesses = []
        for attempt in range(1, self.attempts + 1):
            guess = self.make_guess(previous_guesses)
            feedback = self.wordle_game.get_feedback(guess, self.wordle_game.target_word)
            previous_guesses.append(guess)
            print(f"Attempt {attempt}: Guess = {guess}, Feedback = {feedback}")
            if guess == self.wordle_game.target_word:
                print(f"Congratulations! You've won in {attempt} tries.")
                return attempt
            self.filter_possible_words(guess, feedback)
        print("Sorry, you've used all attempts.")
        return self.attempts + 1

class TreeNode:
    def __init__(self, possible_words, guesses):
        self.possible_words = possible_words
        self.guesses = guesses