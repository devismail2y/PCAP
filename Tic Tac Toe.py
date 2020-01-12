board = list(range(1, 10))
def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
mult = 0
for i in range (13):
    if i % 4 == 0 :
        print ("+-------+-------+-------+")
    if i % 4 == 1 or i % 4 == 3 :
        print ("|       |       |       |")
    if i % 4 == 2 :
        print ("|  ",board[mult*3],"  |  ", board[mult*3+1],"  |  ",board[mult*3+2], "  |")
        mult += 1
        
def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def DrawMove(board):
#
# the function draws the computer's move and updates the board
#