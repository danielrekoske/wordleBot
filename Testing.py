from WordleBot import WordleBot

class Testing:
    def __init__(self, wordle_game):
        self.wordle_game = wordle_game

    def test_bot(self):
        total_attempts = 0
        for answer in self.wordle_game.answers[:100]:
            self.wordle_game.target_word = answer
            bot = WordleBot(self.wordle_game)
            attempts = bot.play()
            total_attempts += attempts
        average_attempts = total_attempts / len(self.wordle_game.answers[:100])
        print(f"Average number of attempts: {average_attempts:.2f}")
