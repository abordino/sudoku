# Sudoku_laburd
Solving sudoku implementing a simple version of DFS.
Sudoku's are assumed to have one and one only solution. It consists of four main functions:
- choose_square: choose which square to fill.
- evaluate_options: check the availavble options for that square.
- complete_square: fill the square with an available option, if any.
- backtracking: once the choice you made leads you to a dead-end, it brings you back to the last guess and tries another option.

The most difficult (???) solved in 10 seconds: https://www.focus.it/tecnologia/digital-life/ecco-il-sudoku-piu-difficile-del-mondo-123-6132-81

It required 10969 iterations.

![](https://www.focus.it/site_stored/imgs/0001/011/sudokuinkala.630x360.jpg)
