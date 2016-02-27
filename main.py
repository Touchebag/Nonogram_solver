from enum import Enum

row_numbers = [[3], [1, 1, 1], [2], [2], [1, 2]]
col_numbers = [[2], [1, 1], [2], [3], [4]]

Square = Enum('Square', 'unknown empty filled')

class Nonogram():
    nonogram = [];

    def __init__(self, n_rows, n_cols):
        self.nonogram = [[Square.unknown for x in range(n_cols)]
                                         for y in range(n_rows)]

    def print_nonogram(self):
        output = [''.join([self.square_to_string(x) for x in row]) for row in self.nonogram]
        output_string = '\n'.join(output)
        print(output_string)

    @staticmethod
    def square_to_string(square):
        if square == Square.unknown:
            return 'k'
        elif square == Square.empty:
            return 'x'
        elif square == Square.filled:
            return '#'


n = Nonogram(len(row_numbers), len(col_numbers))

n.print_nonogram()

