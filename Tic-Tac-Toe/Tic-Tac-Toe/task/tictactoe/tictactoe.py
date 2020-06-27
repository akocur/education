class TicTacToe:

    def __init__(self, data='_'):
        self.cells = [[data[i * 3 + j] for j in range(3)] for i in range(3)]
        self.state = 'Game not finished'
        self.players = {'X': [False, 0],  # [is_win, count]
                        'O': [False, 0]}

    def display(self):
        print('---------')
        for i in range(3):
            print('|', end=' ')
            for j in range(3):
                print(self.cells[i][j], end=' ')
            print('|')
        print('---------')

    def checks_is_player_winner(self, player):
        for row in self.cells:
            number_in_row = sum([1 if cell == player else 0 for cell in row])
            if number_in_row == 3:
                self.players[player][0] = True
                return

        columns = [[self.cells[r][c] for r in range(3)] for c in range(3)]
        for column in columns:
            number_in_column = sum([1 if cell == player else 0 for cell in column])
            if number_in_column == 3:
                self.players[player][0] = True
                return

        diagonals = [[self.cells[i][i] for i in range(3)], [self.cells[i][2 - i] for i in range(3)]]
        for diagonal in diagonals:
            number_in_diagonal = sum(1 if cell == player else 0 for cell in diagonal)
            if number_in_diagonal == 3:
                self.players[player][0] = True
                return

    def sets_state(self):
        self.state = 'Game not finished'
        self.checks_is_player_winner('X')
        self.checks_is_player_winner('O')
        for row in self.cells:
            for cell in row:
                if cell == '_':
                    continue
                self.players[cell][1] += 1  # incriment count
        if self.players['X'][0] == self.players['O'][0] == True \
                or abs(self.players['X'][1] - self.players['O'][1]) > 1:
            self.state = 'Impossible'
        elif self.players['X'][0]:
            self.state = 'X wins'
        elif self.players['O'][0]:
            self.state = 'O wins'
        elif self.players['X'][1] + self.players['O'][1] == 9:
            self.state = 'Draw'

    def is_correct_coordinates(self, coordinates):
        if not len(coordinates) == 2:
            print('There should be two coordinates!')
            return False
        for coordinate in coordinates:
            if not coordinate.isdigit():
                print('You should enter numbers!')
                return False
            if int(coordinate) not in range(1, 4):
                print('Coordinates should be from 1 to 3!')
                return False
        return True

    def enter_coordinates(self):
        while True:
            coordinates = input('Enter the coordinates: > ').split()
            if not self.is_correct_coordinates(coordinates):
                continue
            column, row = int(coordinates[0]) - 1, 3 - int(coordinates[1])
            if not self.cells[row][column] == '_':
                print('This cell is occupied! Choose another one!')
                continue
            self.cells[row][column] = 'X'
            break

    def play(self):
        self.sets_state()
        self.display()
        self.enter_coordinates()
        self.sets_state()
        self.display()


input_data = input('Enter cells: > ')
game = TicTacToe(input_data)
game.play()
