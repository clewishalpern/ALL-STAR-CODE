from Myro import *
init ("sim")
sim = Simulation("Empty Room", 500, 500, makeColor("green"))
sim.setup()
makeRobot("SimScribbler", sim)
#e by Christina
#can't figure out why color function isn't working
penDown ("green")
#found right numbers through trial and error
x=.7
y=1
z=4
#keep variable ratios the same, but can control size
#of the letter
def e ():
    turnBy(15,"deg")
    motors (x,y,z)
    turnBy(80,"deg")
    motors (-x,y,z*.5)
    #turnBy(1,"deg")
   # motors (-x,y,z*.3)
    motors (-x*.3,y+1,z*1.5)
    #next step would be to figure out a loop 
    #to change variable values automatically
for i range (3):
    e ()    
