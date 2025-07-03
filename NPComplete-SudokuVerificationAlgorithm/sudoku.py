## Program: sudoku.py
## Author: Theresa Bolaney 
## Date: 3/8/2021 with updates on 7/3/2025
## Description: This program will print a Sudoku puzzle to the console. The user can enter their answer row by row
## and the program will return whether their answer is correct or incorrect. Rows must be entered in the format
## 1,2,3,4,5,6,7,8,9 etc. The on-screen instructions will elaborate further on what types of values are allowed.
## To run the program, enter "python3 sudoku.py" at the command line. 

#This function creates the puzzle to be solved. Blank spaces are indicated by underline characters.
def createPuzzle():
    puzzle = [["_",6,"_",2,5,"_","_","_",1],[4,1,"_","_",6,"_",3,"_","_"],["_","_","_","_","_",7,"_",9,"_"],
[3,7,8,"_",2,5,"_","_","_"],[2,4,1,"_","_","_",7,5,8],["_","_","_",7,8,"_",2,3,4],
["_",3,"_",8,"_","_","_","_","_"],["_","_",9,"_",4,"_","_",6,3],[5,"_","_","_",3,6,"_",8,"_"]]
    return puzzle

#This function will check that each row contains the values 1 through 9 and return True or False
def checkRows(puzzle):
    for i in range(9):
        row = puzzle[i]
        for counter in range(9):
            if (counter+1) not in row:
                return(False)
    return(True)

#This function will check that each column contains the values 1 through 9 and return True or False
def checkColumns(puzzle):
    for i in range(9):
        column = []
        for j in range(9):
            column.append(puzzle[i][j])
        for counter in range(9):
            if (counter+1) not in column:
                return(False)
    return(True)

#This function is a little trickier than the two above. It must check that each mini-grid (3x3 section) within
#the puzzle only contains the values 1-9. 
def checkMiniGrids(puzzle):
    minigrid = []
    for i in range(3):
        for j in range(3):
            minigrid.append(puzzle[i][j])
    for counter in range(9):
        if (counter+1) not in minigrid:
            return(False)
    return(True)

#If all conditions are met for the rows, columns, and minigrids, then the user wins! Win or lose, the status is printed 
#to the console.
def verifyPuzzle(puzzle):
    if (checkRows(puzzle) and checkColumns(puzzle) and checkMiniGrids(puzzle)):
        print("Congratulations, you win!")
    else:
        print("Sorry, this is not the correct solution. You can play again by restarting the program.")

#This is the main program that runs when the user selects "python3 sudoku.py". 
def runProgram():
    #First we create our hardcoded puzzle
    puzzle = createPuzzle()
    #Next we have to display the puzzle on the console.
    #We do this by going through every value in the puzzle and printing them, but with additional characters such as 
    #pipes and hyphens to create a Sudoku grid.
    for line in puzzle[0:3]:
        holder = ""
        for x in range(3):
            holder = holder + str(line[x])
        holder = holder + "|"
        for x in range(3,6):
            holder = holder + str(line[x])
        holder = holder + "|"
        for x in range(6,9):
            holder = holder + str(line[x])
        print(holder)
    print("-----------")
    for line in puzzle[3:6]:
        holder = ""
        for x in range(3):
            holder = holder + str(line[x])
        holder = holder + "|"
        for x in range(3,6):
            holder = holder + str(line[x])
        holder = holder + "|"
        for x in range(6,9):
            holder = holder + str(line[x])
        print(holder)
    print("-----------")
    for line in puzzle[6:9]:
        holder = ""
        for x in range(3):
            holder = holder + str(line[x])
        holder = holder + "|"
        for x in range(3,6):
            holder = holder + str(line[x])
        holder = holder + "|"
        for x in range(6,9):
            holder = holder + str(line[x])
        print(holder)
    
    #This blank list will hold the user's answers
    userAnswer = []

    #Here we explain how to input the solution row by row and what format is acceptable.
    #Each row is appended to the blank list we just made.
    print("When you have found the solution, please enter it in the console row by row. Separate values by commas.")
    print("The console will prompt you for each line. For example: Row 1: 1,2,3,4,5,6,7,8,9")
    print("Please only enter values 1-9. You may repeat values if you wish. Do not enter")
    print("any strings, more/less than 9 values, etc.")
    for x in range(9):
        print("Row " + str(x+1) + " :")
        row = input()
        newLine = [int(number) for number in row.split(",")]
        userAnswer.append(newLine)

    #Finally we take the user's input list and send it to our verification algorithm
    verifyPuzzle(userAnswer)

runProgram()
