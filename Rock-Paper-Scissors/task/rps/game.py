import random


class RockPaperScissors:
    lose_options = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

    def __init__(self, user_choice):
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])
        self.user_choice = user_choice
        self.status = None

    def set_status(self):
        if RockPaperScissors.lose_options[self.user_choice] == self.computer_choice:
            self.status = 'lose'
        elif self.computer_choice == self.user_choice:
            self.status = 'draw'
        else:
            self.status = 'win'

    def prints_result(self):
        statuses = {'lose': f'Sorry, but computer chose {self.computer_choice}',
                    'draw': f'There is a draw ({self.computer_choice})',
                    'win': f'Well done. Computer chose {self.computer_choice} and failed'}
        print(statuses[self.status])

    def play(self):
        self.set_status()
        self.prints_result()


game = RockPaperScissors(input())
game.play()
