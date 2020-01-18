board = list(range(1, 10))
board = [tuple(board[x:x+3]) for x in range(0, len(board), 3)]
winner = False
move = 0

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

for val1 in range (3) :
    if board[val1][0] == board[val1][1] == board[val1][2] :
        winner = True
        who = board[val1][0]
    elif board[0][val1] == board[1][val1] == board[2][val1] :
        winner = True
        who = board[0][val1]
    elif board[0][0] == board[1][1] == board[2][2] :
        winner = True
        who = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]
        winner = True
        who = board[0][2]

if winner == True :
    print (who, "is the winner!")


def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
free = []
if board[1][1] != "X" :
    board[1][1] = "X"
else : 

 


