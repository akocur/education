from math import sqrt
import random
import sys

class Player:
    def __init__(self, hero, level='user'):
        self.hero = hero
        self.level = level
        self.is_computer = level in ('easy', 'medium', 'hard')


class TicTacToe:
    n_rows = 3
    X = 'X'
    O = 'O'
    empty_cell = '_'

    def __init__(self, player_1, player_2, cells=None):
        self.player_1 = player_1
        self.player_2 = player_2
        if cells is None:
            cells = TicTacToe.empty_cell * TicTacToe.n_rows ** 2
        else:
            TicTacToe.n_rows = int(sqrt(len(cells)))
        self.cells = [list(cells[i:i + TicTacToe.n_rows]) for i in range(0, TicTacToe.n_rows ** 2, TicTacToe.n_rows)]
        if cells.count(player_1.hero) == cells.count(player_2.hero):
            self.current_player = player_1 if player_1.hero == TicTacToe.X else player_2
        else:
            self.current_player = player_2 if cells.count(player_1.hero) > cells.count(player_2.hero) else player_1
        self.state = None
        self.set_state()

    def __str__(self):
        return '-' * TicTacToe.n_rows ** 2 + '\n| '\
               + ' |\n| '.join([' '.join(self.cells[i]) for i in range(TicTacToe.n_rows)]) + ' |\n'\
               + '-' * TicTacToe.n_rows ** 2

    def get_computer_coordinates(self):
        free_cells = self.get_free_cells()
        if self.current_player.level == 'easy':
            return random.choice(free_cells)
        if self.current_player.level == 'medium':
            current_player_winning_coordinates = []
            opponent = self.get_opponent()
            opponent_winning_coordinates = []
            for r in range(TicTacToe.n_rows):
                if self.cells[r].count(TicTacToe.empty_cell) == 1:
                    if self.cells[r].count(self.current_player.hero) == len(self.cells[r]) - 1:
                        current_player_winning_coordinates.append((r, self.cells[r].index(TicTacToe.empty_cell)))
                    if self.cells[r].count(opponent.hero) == len(self.cells[r]) - 1:
                        opponent_winning_coordinates.append((r, self.cells[r].index(TicTacToe.empty_cell)))
            if current_player_winning_coordinates:
                return current_player_winning_coordinates[0]
            if opponent_winning_coordinates:
                return opponent_winning_coordinates[0]
            return random.choice(free_cells)
        if self.current_player.level == 'hard':
            if len(free_cells) == TicTacToe.n_rows ** 2:
                return TicTacToe.n_rows // 2, TicTacToe.n_rows // 2
            current_player = self.current_player
            state = self.state
            best_score = -sys.maxsize
            for r, c in free_cells:
                self.make_move(r, c)
                self.set_state()
                score = self.min_max(current_player)
                if best_score < score:
                    best_score = score
                    row, column = r, c
                self.cells[r][c] = TicTacToe.empty_cell
                self.current_player = current_player
                self.state = state
            return row, column
        return free_cells[0]

    def get_free_cells(self):
        return [(r, c) for r in range(TicTacToe.n_rows)
                for c in range(TicTacToe.n_rows) if self.cells[r][c] == TicTacToe.empty_cell]

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
        self.cells[row][column] = self.current_player.hero
        self.current_player = self.get_opponent()

    def min_max(self, ai):
        opponent = self.player_1 if ai == self.player_2 else self.player_2
        if self.state == 'Draw':
            return 0
        if self.state == f'{ai.hero} wins':
            return 1
        if self.state == f'{opponent.hero} wins':
            return -1

        score = -sys.maxsize if self.current_player == ai else sys.maxsize
        for r, c in self.get_free_cells():
            current_player = self.current_player
            self.make_move(r, c)
            self.set_state()
            if current_player == ai:
                score = max(score, self.min_max(ai))
            else:
                score = min(score, self.min_max(ai))
            self.cells[r][c] = TicTacToe.empty_cell
            self.current_player = current_player
            self.set_state()
        return score

    def get_opponent(self):
        return self.player_1 if self.current_player == self.player_2 else self.player_2

    def play(self):
        while self.state == 'Game not finished':
            print(self)
            if self.current_player.is_computer:
                print(f'Making move level "{self.current_player.level}"')
                coordinates = self.get_computer_coordinates()
            else:
                coordinates = input('Enter the coordinates: > ').strip().split()
                while not self.is_correct_coordinates(coordinates):
                    coordinates = input('Enter the coordinates: > ').strip().split()
                coordinates = len(self.cells) - int(coordinates[1]), int(coordinates[0]) - 1
            self.make_move(coordinates[0], coordinates[1])
            self.set_state()
        print(self, self.state, sep='\n')

    def set_state(self):
        columns = [[self.cells[r][c] for r in range(TicTacToe.n_rows)] for c in range(TicTacToe.n_rows)]
        diagonals = [[self.cells[d][d] for d in range(TicTacToe.n_rows)],
                     [self.cells[d][TicTacToe.n_rows - d - 1] for d in range(TicTacToe.n_rows)]]
        for hero in [self.player_1.hero, self.player_2.hero]:
            for collection in [self.cells, columns, diagonals]:
                if any(c.count(hero) == TicTacToe.n_rows for c in collection):
                    self.state = f'{hero} wins'
                    return
        if any(TicTacToe.empty_cell in r for r in self.cells):
            self.state = 'Game not finished'
        else:
            self.state = 'Draw'


def main():
    answer = input('Input command: > ')
    levels = ('easy', 'medium', 'hard', 'user')
    while answer != 'exit':
        command = answer.split()
        if len(command) != 3 or command[0] != 'start' or command[1] not in levels or command[2] not in levels:
            print('Bad parameters!')
            answer = input('Input command: > ')
            continue
        game = TicTacToe(Player('X', command[1]), Player('O', command[2]))
        game.play()
        answer = input('\nInput command: > ')


if __name__ == '__main__':
    main()
