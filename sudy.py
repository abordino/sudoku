import numpy as np

""" A sudoku is simply a list. Each element of the list is a list which contains four elements:
- a sudoku (list): the evolution of the sudoku to solve in time
- a list of two int (list(int)): the coordinates of the square chosen to be filled
- a list of integer list(int): the options available for those coordinates.
"""


def chunks(n_n_list):
    """ Converts list of 81 integers in a matrix 9x9.

           Args_1:
             n_n_list (list): list of 81 integers to be converted.

           Returns:
             matrix (list): the list write as a 9x9 matrix
    """
    matrix = [n_n_list[k:k + 9] for k in range(0, len(n_n_list), 9)]
    return matrix


def norm_last_sudoku(sudoku):
    """Converts the last sudoku in 0/1.

       Args_1:
         sudoku (list): sudoku to be solved.

       Returns:
         normalized_sudoku (np.array) : the normalized sudoku.
       """
    last_sudoku = np.array(sudoku[-1][0]) > 0
    normalized_sudoku = np.array(last_sudoku).astype(np.int)
    return normalized_sudoku


def three_squares(sudoku, i, j):
    """Find the number of non empty cells in the 3x3 square the cell [i,j] belongs to (in the last sudoku).

    Args_1:
      sudoku (Sudoku): sudoku to be solved

    Arg_2:
        i, j (int): coordinates of the square

    Returns:
      number_neigh (int) : number of neighbour
      list_1, list_2 (list(int)): location of the 3x3 square
    """

    sudoku_in_use = norm_last_sudoku(sudoku)

    if i in [0, 1, 2]:
        list_1 = [0, 1, 2]
    elif i in [3, 4, 5]:
        list_1 = [3, 4, 5]
    else:
        list_1 = [6, 7, 8]

    if j in [0, 1, 2]:
        list_2 = [0, 1, 2]
    elif j in [3, 4, 5]:
        list_2 = [3, 4, 5]
    else:
        list_2 = [6, 7, 8]

    three_square = []
    for x in list_1:
        for y in list_2:
            three_square.append(sudoku_in_use[x][y])
    number_neigh = sum(three_square)

    return number_neigh, list_1, list_2


def choose_square(sudoku):
    """Choose which square of the matrix to fill.

    Args:
      sudoku (Sudoku): sudoku to be solved

    Returns:
      [x, y] (list(int)): coordinates of the square to fill
    """
    sudoku_in_use = norm_last_sudoku(sudoku)
    max_score, coordinates = 0, None

    for i in range(9):
        for j in range(9):
            if sudoku_in_use[i, j] != 0:
                pass
            else:
                score_ij = sum(sudoku_in_use[i, :]) + sum(sudoku_in_use[:, j]) - 2 * sudoku_in_use[i, j] + \
                           three_squares(sudoku, i, j)[0]
                if score_ij > max_score:
                    max_score = score_ij
                    coordinates = [i, j]
    return coordinates


def evaluate_options(sudoku, coordinates):
    """Evaluate the options available to the coordinates chosen.

    Args_1:
      sudoku (Sudoku): sudoku working on

    Args_2:
      coordinates (list(int)): coordinates chosen with choose_square.

    Returns:
      options: list of element you can fill the square without breaking the rules
    """
    sudoku_in_use = sudoku[-1][0]
    i, j = coordinates[0], coordinates[1]
    list_1, list_2 = three_squares(sudoku, i, j)[1], three_squares(sudoku, i, j)[2]

    set_1 = set(np.array(sudoku_in_use)[i, :])
    set_2 = set(np.array(sudoku_in_use)[:, j])
    set_3 = set(np.array(sudoku_in_use)[list_1[0]:list_1[-1] + 1, list_2[0]:list_2[-1] + 1].flatten())

    element_present = set_1.union(set_2.union(set_3))
    options = list(set(range(10)).difference(element_present))

    return options


def complete_square(sudoku, coordinates, options):
    """Complete the square chosen with choose_square.
       It's either forced or guessed.

    Args_1:
        sudoku (Sudoku): sudoku working on
    Args_2:
        coordinates (list(int)): coordinates of the square to fill
    Args_3:
        options (list(int)): list of the available options
    """
    i, j = coordinates[0], coordinates[1]
    new_sudoku = []
    for h in range(9):
        for k in range(9):
            if [h, k] == [i, j]:
                new_sudoku.append(options[0])
            else:
                new_sudoku.append(sudoku[-1][0][h][k])
    sudoku.append([chunks(new_sudoku), coordinates, options[1:]])


def backtracking(sudoku):
    """If the rules were broken, cut the branches and explore another.

    Args:
      sudoku (list): sudoku working on.
    """
    index = len(sudoku) - 1
    while len(sudoku[index][2]) == 0:
        index -= 1

    last_guess = sudoku[index]
    new_guess = []
    for h in range(9):
        for k in range(9):
            if [h, k] == last_guess[1]:
                new_guess.append(last_guess[2][0])
            else:
                new_guess.append(last_guess[0][h][k])

    del sudoku[index:]
    sudoku.append([chunks(new_guess), last_guess[1], last_guess[2][1:]])


def solve(sudoku):
    """Solve a sudoku, assuming there's only one solution.

    Args:
      sudoku (Sudoku): sudoku to be solved
    """
    iteration = 0
    while 0 in np.array(sudoku[-1][0]):
        iteration += 1
        coord = choose_square(sudoku)
        options = evaluate_options(sudoku, coord)
        if len(options) == 0:
            backtracking(sudoku)
        else:
            complete_square(sudoku, coord, options)
    solution = np.array(sudoku[-1][0])
    return solution, iteration
