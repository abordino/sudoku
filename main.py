from sudoku.sudy import *

if __name__ == '__main__':

    # If you want to receive input from user ->
    #
    # raw_matrix = []
    # for i in range(81):
    #     n = int(input("Write the next element, proceeding by row:"))
    #     raw_matrix.append(n)
    # matrix = chunks(raw_matrix)
    # my_sudoku = [[matrix, 0, 0, 0]]

    matrix = [[0, 0, 5, 3, 0, 0, 0, 0, 0],
              [8, 0, 0, 0, 0, 0, 0, 2, 0],
              [0, 7, 0, 0, 1, 0, 5, 0, 0],
              [4, 0, 0, 0, 0, 5, 3, 0, 0],
              [0, 1, 0, 0, 7, 0, 0, 0, 6],
              [0, 0, 3, 2, 0, 0, 0, 8, 0],
              [0, 6, 0, 5, 0, 0, 0, 0, 9],
              [0, 0, 4, 0, 0, 0, 0, 3, 0],
              [0, 0, 0, 0, 0, 9, 7, 0, 0]]

    my_sudoku = [[matrix, [], []]]
    solution, moves = solve(my_sudoku)
    print(" \t The solution is: \n", solution, "\n \t It required", moves, "moves.")
