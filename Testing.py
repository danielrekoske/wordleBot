from WordleBot import WordleBot

class Testing:
    def __init__(self, wordle_game):
        self.wordle_game = wordle_game

    def test_bot(self):
        total_attempts = 0
        counter = 0
        for answer in self.wordle_game.answers:
            counter += 1
            if counter % 100 == 0:
                print(counter)
            self.wordle_game.target_word = answer
            bot = WordleBot(self.wordle_game)
            attempts = bot.play()
            total_attempts += attempts
        average_attempts = total_attempts / len(self.wordle_game.answers)
        print(f"Average number of attempts: {average_attempts:.2f}")
