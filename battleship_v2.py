from random import *
from Processing import *

board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
ship = 2
board[randint(0,4)][randint(0,4)] = ship

#prints where the battleship is each time.
print(board)
def setup():
    size(500,500)
    background(255,0,0)
    global board 
#have to call setup function when processing in calico
#draws first row
    for i in range(len(board[0])):
        if (board[0][i] == 0 or 2 ):
           fill(255)
           rect(i*100, 0, 100, 100)
    #draws second row and so on 
    for i in range(len(board[1])):
        if (board[1][i] == 0 or 2):
            rect(i*100, 100, 100, 100)
    for i in range(len(board[2])):
        if (board[2][i] == 0 or 2):
            rect(i*100, 200, 100, 100)
    for i in range(len(board[0])):
        if (board[3][i] == 0 or 2 ):
            rect(i*100, 300, 100, 100)
    for i in range(len(board[0])):
        if (board[4][i] == 0 or 2 ):
            rect(i*100, 400, 100, 100)

"""def draw():
    rect(0,0,100,100)    
draw()"""
#sets number of guesses allowed
setup()
#x is variable that counts tries
x = 0
# y is fixed number of tries player gets
y = 15
while x < y :
    row = int(input ("guess a row (0 - 4)"))
    column = int(input ("guess a column (0 - 4)"))
    #try again. no way yet to restart game if you lose.
    if (board[row][column] != 2):
        fill(50)
        rect(column*100,row*100, 100, 100)
        x = x + 1
#you have sunk my battleship!
    elif (board[row][column] == 2):
        fill (0,255,0)
        rect(column*100,row*100,100,100)
        again = int(input ("you won! want to play again? yes = 1, no = 2"))
        #restarts the game
        if again == 1:
            x = 0
            setup()
        #ends the game
        else:
            x = y
           
    
