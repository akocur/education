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
        new_matrix = None
        if isinstance(other, int) or isinstance(other, float):
            new_matrix = Matrix(self.number_of_rows, self.number_of_columns)
            new_matrix.table = [[self.table[i][j] * other for j in range(self.number_of_columns)]
                                for i in range(self.number_of_rows)]
        return new_matrix

    def __str__(self):
        s = '\n'
        for row in self.table:
            for x in row:
                s += str(x) + ' '
            s = s[:-1] + '\n'
        return s

    def read(self):
        self.table = [[int(x) for x in input().split()[:self.number_of_columns]] for _i in range(self.number_of_rows)]


A = Matrix(*input().split())
A.read()
B = A * int(input())
print(B)
