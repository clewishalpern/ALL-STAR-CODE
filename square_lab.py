## christina's code. 
## got to figure out how to do a line breakpen
from Myro import * 
init ("sim")
##lines 6-10 draw a P
penDown ("red")
for i in range(5):
    forward(1, 1)
    turnBy(60,"deg")
forward(1, 1)
def drawsquare ():
    for i in range(3):
        forward(1, 1)
        turnBy(90,"deg")
    forward(1, 1)
drawsquare ()
forward(1, 1)
drawsquare ()
forward(1, .5)
drawsquare ()