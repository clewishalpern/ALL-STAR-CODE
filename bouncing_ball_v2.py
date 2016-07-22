from random import *
from Processing import *

x = 200
y = 200
yspeed = 7
xspeed = 4
dir = 1



def setup():
    size(400, 400)

def draw():
    global x
    global y
    global xspeed
    global yspeed
    global dir
    #img = loadImage("Christina_pic.jpg")
    
    background(255)
    #image(img,x,y)
    fill (255,0,0)
    ellipse(x,y,50,50)
    
    x = xspeed + x
    y = yspeed + y
    if x >375 or x<25:
        xspeed = xspeed * -1
    if y < 25 or y>375:
        yspeed = yspeed * -1
setup () 
while True:
    draw()
    delay (10)


    