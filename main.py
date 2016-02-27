from enum import Enum
import itertools

col_numbers = [[2], [1, 1], [1, 2], [1, 1], [2]]
row_numbers = [[1], [1, 1], [1, 1], [1, 1, 1], [1]]

Square = Enum('Square', 'unknown empty filled')

# TODO remove
ex_row=[Square.unknown,Square.unknown,Square.filled,Square.unknown,Square.filled,Square.filled,Square.filled,Square.unknown,Square.filled,Square.unknown,Square.unknown,Square.unknown,Square.unknown]
ex_num=[1,3,1]

class Nonogram():
    nonogram = [];

    def __init__(self, n_rows, n_cols):
        self.nonogram = [[Square.unknown for x in range(n_cols)]
                                         for y in range(n_rows)]

    def print_nonogram(self):
        output = [''.join([self.square_to_string(x) for x in row]) for row in self.nonogram]
        output_string = '\n'.join(output)
        # print(output_string)
        # self.check_line(col_numbers[1], self.nonogram[1])
        self.check_line(ex_num, ex_row)

    @staticmethod
    def square_to_string(square):
        if square == Square.unknown:
            return 'k'
        elif square == Square.empty:
            return 'x'
        elif square == Square.filled:
            return '#'

    @staticmethod
    def check_line(numbers, line):
        grouped_row = [list(g) for k, g in itertools.groupby(line)]
        filled_squares = [len(x) for x in grouped_row if x[0] == Square.filled]
        return filled_squares == numbers



n = Nonogram(len(row_numbers), len(col_numbers))

n.print_nonogram()

