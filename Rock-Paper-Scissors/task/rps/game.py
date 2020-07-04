import random


class RockPaperScissors:
    instruments = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
                   'dragon', 'devil', 'lightning', 'gun']

    def __init__(self, rating_file_name='rating.txt'):
        self.instruments = ['rock', 'scissors', 'paper']
        self.losing_options = {}
        self.computer_choice = None
        self.user_choice = None
        self.status = None
        self.rating_file_name = rating_file_name
        self.user_name = None
        self.user_rating = None
        file = open(self.rating_file_name, 'r')
        self.user_list = file.readlines()
        file.close()
        self.user_index_in_list = -1

    def play(self):
        self.user_name = input('Enter your name: ').strip().capitalize()
        print(f'Hello, {self.user_name}')
        self.sets_user_rating_from_file()
        self.sets_instruments(input().split(','))
        self.sets_losing_options()
        print("Okay, let's start")
        self.user_choice = input().strip()
        while not self.user_choice == '!exit':
            if self.user_choice == '!rating':
                print(f'Your rating: {self.user_rating}')
                self.user_choice = input().strip()
                continue
            if self.user_choice not in self.instruments:
                print('Invalid input')
                self.user_choice = input().strip()
                continue
            self.computer_choice = random.choice(self.instruments)
            self.sets_status()
            self.sets_user_rating()
            self.prints_result()
            self.user_choice = input().strip()
        print('Bye!')
        self.saves_user_rating_in_file()

    def prints_result(self):
        statuses = {'lose': f'Sorry, but computer chose {self.computer_choice}',
                    'draw': f'There is a draw ({self.computer_choice})',
                    'win': f'Well done. Computer chose {self.computer_choice} and failed'}
        print(statuses[self.status])

    def saves_user_rating_in_file(self):
        if self.user_index_in_list >= 0:
            file = open(self.rating_file_name, 'w')
            self.user_list[self.user_index_in_list] = f'{self.user_name} {self.user_rating}\n'
            file.writelines(self.user_list)
        else:
            file = open(self.rating_file_name, 'a')
            file.write(f'{self.user_name} {self.user_rating}\n')
        file.close()

    def sets_instruments(self, options):
        if len(options) > 1:
            self.instruments = [instrument for instrument in RockPaperScissors.instruments if instrument in options]

    def sets_losing_options(self):
        instruments = RockPaperScissors.instruments
        for instrument in instruments:
            if instrument in self.instruments:
                index = self.instruments.index(instrument)
                self.losing_options[instrument] = instruments[index + 8:] + instruments[max(0, index - 7):index]

    def sets_status(self):
        if self.computer_choice in self.losing_options[self.user_choice]:
            self.status = 'lose'
        elif self.computer_choice == self.user_choice:
            self.status = 'draw'
        else:
            self.status = 'win'

    def sets_user_rating(self):
        if self.status == 'draw':
            self.user_rating += 50
        elif self.status == 'win':
            self.user_rating += 100

    def sets_user_rating_from_file(self):
        self.user_rating = 0
        index = -1
        for line in self.user_list:
            index += 1
            if self.user_name in line:
                self.user_rating = int(line.split()[1])
                self.user_index_in_list = index
                break


game = RockPaperScissors()
game.play()
