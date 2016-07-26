from Myro import *
init ("sim")
penDown ("white")
for i in range (78):
    forward (.8, .3)
    turnBy (5, "deg")
penUp ()
for i in range (12):
    forward (.8, .3)
    turnBy (5, "deg")
turnBy (90, "deg")
penDown ("red")
forward (2, 2.5)