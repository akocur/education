class Matrix:
    def __init__(self, number_of_rows, number_of_columns):
        self.number_of_rows = int(number_of_rows)
        self.number_of_columns = int(number_of_columns)
        self.table = None

    def __add__(self, other):
        if not (type(other) == type(self) and
                (self.number_of_rows == other.number_of_rows and self.number_of_columns == other.number_of_columns)):
            return None

        new_matrix = Matrix(self.number_of_rows, self.number_of_columns)
        new_matrix.table = [[self.table[i][j] + other.table[i][j] for j in range(self.number_of_columns)]
                            for i in range(self.number_of_rows)]
        return new_matrix

    def __mul__(self, other):
        matrix = None
        if isinstance(other, int) or isinstance(other, float):
            matrix = Matrix(self.number_of_rows, self.number_of_columns)
            matrix.table = [[self.table[i][j] * other for j in range(self.number_of_columns)]
                            for i in range(self.number_of_rows)]
        if isinstance(other, Matrix):
            if not self.number_of_columns == other.number_of_rows:
                return None
            matrix = Matrix(self.number_of_rows, other.number_of_columns)
            matrix.table = []
            for n in range(self.number_of_rows):
                matrix.table.append([])
                for m in range(other.number_of_columns):
                    matrix.table[n].append(sum(self.table[n][i] * other.table[i][m]
                                               for i in range(self.number_of_columns)))

        return matrix

    def __str__(self):
        s = ''
        for row in self.table:
            for x in row:
                s += str(x) + ' '
            s = s[:-1] + '\n'
        return s

    def read(self):
        self.table = [[float(x) if x.count('.') else int(x) for x in input().split()[:self.number_of_columns]]
                      for _i in range(self.number_of_rows)]


class Menu:
    def __init__(self):
        self.menu = {
            '1': ['\n1. Add matrices', self.add_matrices],
            '2': ['2. Multiply matrix by a constant', self.multiply_matrix_by_constant],
            '3': ['3. Multiply matrices', self.multiply_matrices],
            '0': ['0. Exit', None],
        }

    @staticmethod
    def add_matrices():
        first_matrix = Menu.create_matrix('first')
        second_matrix = Menu.create_matrix('second')
        Menu.print_result(first_matrix + second_matrix)

    @staticmethod
    def create_matrix(number=''):
        dimensions = input(f'Enter size of {number}{" " if number else ""}matrix: > ').split()
        matrix = Matrix(dimensions[0], dimensions[1])
        print(f'Enter {number}{" " if number else ""}matrix:')
        matrix.read()
        return matrix

    @staticmethod
    def multiply_matrices():
        first_matrix = Menu.create_matrix('first')
        second_matrix = Menu.create_matrix('second')
        Menu.print_result(first_matrix * second_matrix)

    @staticmethod
    def multiply_matrix_by_constant():
        matrix = Menu.create_matrix()
        const = input('Enter constant: > ')
        const = float(const) if const.count('.') else int(const)
        Menu.print_result(matrix * const)

    def print_menu(self):
        menu = tuple(self.menu.values())
        for item in menu:
            print(item[0])
        return input('Your choice: > ')

    @staticmethod
    def print_result(result=None):
        print('The operation cannot be performed.' if result is None else 'The result is:\n', result)

    def run(self):
        answer = self.print_menu()
        while not answer == '0':
            item = self.menu.get(answer, None)
            if item is None:
                print('There is no such item\n')
                answer = self.print_menu()
                continue
            function = item[1]
            function()
            answer = self.print_menu()


Menu().run()
