
#christina and swarup's code
r=color (255,0,0)
o=color (237,142,17)
y=color (237,237,17)
g=color (0,255,0)
b=color (0,0,255)
p=color (200,10,200)
w=color (255,255,255)
blck=color (0,0,0)
myColors=[r,o,y,g,b,p,w,blck]
#"orange","yellow","green","blue","purple","black","white"]
pickColor = 0
def setup ():
    size(400,600)
def draw ():
    global myColors
    for i in range(len(myColors)):
        fill (myColors[i])
        rect(i*50,0,50,50)

    if mouseButton == LEFT :
        x=50
        for i in range(len(myColors)):
            if mouseY < x :
                global pickColor
                if mouseX >i*50 and mouseX <=(i*50)+50 :
                    pickColor = i                
            else :
                fill (myColors[pickColor])
                ellipse(mouseX,mouseY,5,5)
#less than 36 lines of code!!!!!