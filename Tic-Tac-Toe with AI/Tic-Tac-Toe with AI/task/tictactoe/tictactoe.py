from math import sqrt


class TicTacToe:
    n_rows = 3
    player_x = 'X'
    player_o = 'O'
    empty_cell = '_'

    def __init__(self, cells=None):
        if cells is None:
            cells = TicTacToe.empty_cell * TicTacToe.n_rows ** 2
        else:
            TicTacToe.n_rows = int(sqrt(len(cells)))
        self.cells = [list(cells[i:i + TicTacToe.n_rows]) for i in range(0, TicTacToe.n_rows ** 2, TicTacToe.n_rows)]
        self.current_player = TicTacToe.player_o if cells.count(TicTacToe.player_x) \
                                                    > cells.count(TicTacToe.player_o) else TicTacToe.player_x
        self.state = None
        self.set_state()

    def __str__(self):
        return '-' * TicTacToe.n_rows ** 2 + '\n| '\
               + ' |\n| '.join([' '.join(self.cells[i]) for i in range(TicTacToe.n_rows)]) + ' |\n'\
               + '-' * TicTacToe.n_rows ** 2

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
        # while self.state == 'Game not finished':
        print(self)
        coordinates = input('Enter the coordinates: > ').strip().split()
        while not self.is_correct_coordinates(coordinates):
            coordinates = input('Enter the coordinates: > ').strip().split()
        self.make_move(len(self.cells) - int(coordinates[1]), int(coordinates[0]) - 1)
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
    game = TicTacToe(input('Enter cells: > '))
    game.play()


if __name__ == '__main__':
    main()
