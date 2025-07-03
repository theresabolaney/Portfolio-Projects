# NPComplete-SudokuVerificationAlgorithm
CS 325 Analysis of Algorithms portfolio project. A Sudoku verification algorithm (solution checking program) written in Python. The program displays a Sudoku puzzle, waits for a user's input to a possible solution, then checks if the solution is correct in O(n) time.

Sudoku Puzzle Project.pdf contains a thorough explanation of the program, its run time, and a bonus hypothesis on how to form a true Sudoku solver program rather than a verification program. 

sudoku.py: To run the program, enter "python3 sudoku.py" at the console. There should not be any additional dependencies or libraries needed; please contact me if that doesn't turn out to be the case. 

Follow the onscreen prompts to play the game but please be aware that there is no input verification when the user enters
their solution. Please only enter values 1-9, do not enter more/less than 9 numbers, and do not enter strings. Separate
all values by commas.

The puzzle is hardcoded in the function createPuzzle. The solution is pasted below if you would like to use it for 
testing the program. Please be aware of hidden newline characters if you copy/paste directly from here.

9,6,3,2,5,4,8,7,1

4,1,7,9,6,8,3,2,5

8,5,2,3,1,7,4,9,6

3,7,8,4,2,5,6,1,9

2,4,1,6,9,3,7,5,8

6,9,5,7,8,1,2,3,4

1,3,6,8,7,9,5,4,2

7,8,9,5,4,2,1,6,3

5,2,4,1,3,6,9,8,7
