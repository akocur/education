import random


class RockPaperScissors:
    lose_options = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
    instruments = ['rock', 'paper', 'scissors']

    def __init__(self, rating_file_name='rating.txt'):
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
        self.user_choice = input().strip()
        while not self.user_choice == '!exit':
            if self.user_choice == '!rating':
                print(f'Your rating: {self.user_rating}')
                self.user_choice = input().strip()
                continue
            if self.user_choice not in RockPaperScissors.instruments:
                print('Invalid input')
                self.user_choice = input().strip()
                continue
            self.computer_choice = random.choice(RockPaperScissors.instruments)
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

    def sets_status(self):
        if RockPaperScissors.lose_options[self.user_choice] == self.computer_choice:
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
