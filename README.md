# Sudoku-Solver
Functional program that solves a Sudoku problem using backtracking algorithm.

BACKTRACKING ALGORITHM
Backtracking:
1. Pick an empty square
2. Try all possible numbers
3. Identify one that works (based on Sudoku rules e.g. only 1 unique number per row, column, square/grid)
4. Repeat above steps for the next empty square
5. When reached a square where number is invalid, backtrack to previous square and exhaust remaining numbers.
6. If number is still invalid, backtrack again and repeat

Essentially, we are completing one square at a time and recursively checking if the solution works until we reach one that works. Backtrack to previous one if it is invalid. More efficient and effective than the naive approach of forcifully checking every square and manually repeating entire sudoku to solve it.

SOLVER-SET-SUDOKU
 - Utilises backtracking to solve a pre-determined sudoku board. Contains all necessary functions to showcase how it works.

 RANDOM-SUDOKU
 - Randomly generates a board based on sudoku rules and then solves such board. Expands upon previous program.

