from nonogram import Square, Nonogram

col_num = [[2], [1, 1], [1, 2], [1, 1], [2]]
row_num = [[1], [1, 1], [1, 1], [1, 1, 1], [1]]

n = Nonogram(row_num, col_num)

n.print_nonogram()

