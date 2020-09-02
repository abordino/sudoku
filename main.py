from sudoku import sudy as s

if __name__ == '__main__':

    print("Write each element of the sudoku (write 0 in case of an empty cell). \nProceed by row.")
    raw_matrix = []
    for i in range(81):
        n = int(input("Write the next element:"))
        raw_matrix.append(n)
    matrix = s.chunks(raw_matrix)
    my_sudoku = [[matrix, 0, 0, 0]]

    solution, moves = s.solve(my_sudoku)
    print(" \t The solution is: \n", solution, "\n \t It required", moves, "moves.")
