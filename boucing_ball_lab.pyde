from random import *
x = 200
y = 200
yspeed = 6
xspeed = 4
dir = 1
img = loadImage("christina_pic.jpg")



def setup():
    size(400, 400)

def draw():
    global x
    global y
    global xspeed
    global yspeed
    global dir
    global img
    
    background(255)

    image(img,0,0)
    ellipse(x,y,50,50)
    
    x = xspeed + x
    y = yspeed + y
    if x >375 or x<25:
        xspeed = xspeed * -1
    if y < 25 or y>375:
        yspeed = yspeed * -1
    
    

    