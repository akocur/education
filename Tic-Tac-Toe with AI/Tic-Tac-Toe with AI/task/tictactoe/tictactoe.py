from math import sqrt
import random


class TicTacToe:
    n_rows = 3
    player_x = 'X'
    player_o = 'O'
    empty_cell = '_'

    def __init__(self, cells=None, level='easy', user1=None, user2=None):
        if cells is None:
            cells = TicTacToe.empty_cell * TicTacToe.n_rows ** 2
        else:
            TicTacToe.n_rows = int(sqrt(len(cells)))
        self.cells = [list(cells[i:i + TicTacToe.n_rows]) for i in range(0, TicTacToe.n_rows ** 2, TicTacToe.n_rows)]
        self.current_player = TicTacToe.player_o if cells.count(TicTacToe.player_x) \
                                                    > cells.count(TicTacToe.player_o) else TicTacToe.player_x
        self.state = None
        self.set_state()
        self.level = level
        self.user1 = user1
        self.user2 = user2

    def __str__(self):
        return '-' * TicTacToe.n_rows ** 2 + '\n| '\
               + ' |\n| '.join([' '.join(self.cells[i]) for i in range(TicTacToe.n_rows)]) + ' |\n'\
               + '-' * TicTacToe.n_rows ** 2

    def get_computer_coordinates(self):
        free_cells = [(r, c) for r in range(TicTacToe.n_rows)
                      for c in range(TicTacToe.n_rows) if self.cells[r][c] == TicTacToe.empty_cell]
        if self.level == 'easy':
            return random.choice(free_cells)
        return free_cells[0]

    def is_correct_coordinates(self, coordinates):
        if not all(x.isdigit() for x in coordinates):
            print('You should enter numbers!')
            return False
        if not all(int(x) in range(1, TicTacToe.n_rows + 1) for x in coordinates):
            print(f'Coordinates should be from 1 to {TicTacToe.n_rows}!')
            return False
        if not len(coordinates) == 2:
            print('Coordinates should be two!')
            return False
        r, c = len(self.cells) - int(coordinates[1]), int(coordinates[0]) - 1
        if self.cells[r][c] != TicTacToe.empty_cell:
            print('This cell is occupied! Choose another one!')
            return False
        return True

    def make_move(self, row, column):
        self.cells[row][column] = self.current_player
        self.current_player = TicTacToe.player_x if self.current_player == TicTacToe.player_o else TicTacToe.player_o

    def play(self):

        while self.state == 'Game not finished':
            print(self)
            if self.current_player in (self.user1, self.user2):
                coordinates = input('Enter the coordinates: > ').strip().split()
                while not self.is_correct_coordinates(coordinates):
                    coordinates = input('Enter the coordinates: > ').strip().split()
                coordinates = len(self.cells) - int(coordinates[1]), int(coordinates[0]) - 1
            else:
                print(f'Making move level "{self.level}"')
                coordinates = self.get_computer_coordinates()
            self.make_move(coordinates[0], coordinates[1])
            self.set_state()
        print(self, self.state, sep='\n')

    def set_state(self):
        columns = [[self.cells[r][c] for r in range(TicTacToe.n_rows)] for c in range(TicTacToe.n_rows)]
        diagonals = [[self.cells[d][d] for d in range(TicTacToe.n_rows)],
                     [self.cells[d][TicTacToe.n_rows - d - 1] for d in range(TicTacToe.n_rows)]]
        for player in [TicTacToe.player_x, TicTacToe.player_o]:
            for collection in [self.cells, columns, diagonals]:
                if any(c.count(player) == TicTacToe.n_rows for c in collection):
                    self.state = f'{player} wins'
                    return
        if any(TicTacToe.empty_cell in r for r in self.cells):
            self.state = 'Game not finished'
        else:
            self.state = 'Draw'


def main():
    answer = input('Input command: > ')
    while answer != 'exit':
        command = answer.split()
        if len(command) != 3 or command[0] != 'start' or command[1] not in ('easy', 'user')\
                or command[2] not in ('easy', 'user'):
            print('Bad parameters!')
            answer = input('Input command: > ')
            continue
        param = {'user1': None if command[1] == 'easy' else TicTacToe.player_x,
                 'user2': None if command[2] == 'easy' else TicTacToe.player_o}
        game = TicTacToe(**param)
        game.play()
        answer = input('\nInput command: > ')


if __name__ == '__main__':
    main()
