#copied from Alley
from Myro import *
pic = makePicture("christina_pic.jpg")
for p in getPixels(pic):
   #newC = makeColor(getGreen(p),getRed(p),getBlue(p))
   red = makeColor(217,26,33)
   blue = makeColor(112,150,158)
   yellow = makeColor(252,227,166)
   dblue = makeColor(0,51,76)
   if getGray(p) > 180: 
       setColor(p,yellow)
   elif getGray(p) > 120: 
       setColor(p,blue)
   elif getGray(p) > 60: 
       setColor(p,red)
   elif getGray(p) <= 60: 
       setColor(p,dblue)
show(pic)
## show (pic)
## pix = getPixels(pic)
## gray = getGray(pix)
## myList=[pix]
## print (pix)