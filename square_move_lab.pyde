
BOB = 0
dir = 1

def setup():
    size(400, 400)

def draw():
    global BOB
    global dir
    
    if BOB >300 :
        dir = 0
    if BOB < 10:
        dir  = 1
    
    if dir == 0:
        BOB = BOB-1
    else:
        BOB =BOB + 1
    rect(BOB,200,50,50)