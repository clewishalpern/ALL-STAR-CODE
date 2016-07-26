## christina's code. 
## creating a series of smaller squares
from Myro import * 
init ("sim")
x=1
y=1
penDown ("red")
def drawsquare ():
    for i in range(4):
        forward(x,y)
        turnBy(90,"deg")
drawsquare ()
while x>.5:
##picked the x-factor (hahaha) at random.
    drawsquare ()
    x=x*.9
    ##The above will draw 6 squares, i think if x=1.
penUp ()
forward(1,3)
##moving the robot out of the way.


## forward(1, 1)
## def drawsquare ():
##     for i in range(3):
##         forward(1, 1)
##         turnBy(90,"deg")
##     forward(1, 1)
## drawsquare ()
## forward(1, 1)
## drawsquare ()
## forward(1, .5)
## drawsquare ()