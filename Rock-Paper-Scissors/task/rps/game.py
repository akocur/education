import random


class RockPaperScissors:
    lose_options = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
    instruments = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.computer_choice = None
        self.user_choice = None
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
        self.user_choice = input().strip()
        while not self.user_choice == '!exit':
            if self.user_choice not in RockPaperScissors.instruments:
                print('Invalid input')
                self.user_choice = input().strip()
                continue
            self.computer_choice = random.choice(RockPaperScissors.instruments)
            self.set_status()
            self.prints_result()
            self.user_choice = input().strip()
        print('Bye!')


game = RockPaperScissors()
game.play()
