## christina's code. 
## got to figure out how to do a line breakpen
from Myro import * 
init ("sim")
##lines 6-10 draw a triangle
penDown ("red")
for i in range(3):
    forward(1, 1)
    turnBy(120,"deg")
penUp ()
forward (1, 1.25)
penDown ("red")
for i in range(6):
   forward(.8, 1)
   turnBy(60,"deg")
penUp ()
forward (1, 1.5)

  
  