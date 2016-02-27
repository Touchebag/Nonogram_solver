from enum import Enum
import itertools

Square = Enum('Square', 'unknown empty filled')
Unknown = Square.unknown
Empty = Square.empty
Filled = Square.filled

# TODO remove
ex_row=[Square.unknown,Square.unknown,Square.filled,Square.unknown,Square.filled,Square.filled,Square.filled,Square.unknown,Square.filled,Square.unknown,Square.unknown,Square.unknown,Square.unknown]
ex_num=[1,3,1]

# A class representing a nonogram
class Nonogram():
    row_numbers = []
    col_numbers = []
    nonogram = []

    # Initiates with unknown squares
    def __init__(self, rows, cols):
        self.row_numbers = rows
        self.col_numbers = cols
        self.nonogram = [[Square.unknown for x in range(len(cols))]
                                         for y in range(len(rows))]

    # Prints a nonogram
    def print_nonogram(self):
        output = [''.join([square_to_string(x) for x in row]) for row in self.nonogram]
        output_string = '\n'.join(output)

        print(output_string)

    # Checks if the full nonogram is correct
    def check_all_lines(self):
        transposed = [list(x) for x in zip(*self.nonogram)]
        checked_rows = [check_line(self.row_numbers[i], self.nonogram[i])
                        for i in range(len(self.nonogram))]
        checked_cols = [check_line(self.col_numbers[i], transposed[i])
                        for i in range(len(transposed))]

        rows_correct = all(checked_rows)
        cols_correct = all(checked_cols)

        return True == (rows_correct == cols_correct)



# Checks if a line (row/column) has the correct number of filled squares
def check_line(numbers, line):
    grouped_row = [list(g) for k, g in itertools.groupby(line)]
    filled_squares = [len(x) for x in grouped_row if x[0] == Square.filled]
    return filled_squares == numbers

# Converts a Square enum to a string (or char)
def square_to_string(square):
    if square == Square.unknown:
        return 'k'
    elif square == Square.empty:
        return 'x'
    elif square == Square.filled:
        return '#'

