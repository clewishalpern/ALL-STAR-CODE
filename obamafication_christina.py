#by Navid and Christina
from Myro import *
pic = makePicture("christina_pic.jpg")
show (pic)
pix = getPixels(pic)
gray = getGray(pix)
ourpixels=[pix]
print (pix)



## You'll need to use the following functions:
## getPixels(PICTURE)
## getPixels returns a list of individual pixels in the picture you pass. So if you loop through the pixels list, you'll have a pixel you can modify! 
## getRed(PIXEL)
## Returns the red value of a pixel
## getGreen(PIXEL)
## Returns the green value of a pixel
## getBlue(PIXEL)
## Returns the blue value of a pixel
## makeColor(RED,GREEN,BLUE)
## Returns a color to make a pixel from
## setColor(PIXEL, COLOR)
## Sets a pixel to a specific color 
## getGray(PIXEL)
## Gets the gray value of a pixel
## 
## 
## The Obamafication process works as follows: If a pixel's gray value is greater than 180, then change that pixel's color to Obama-Yellow.  If the gray value is greater than 120, then the pixel should be changed to Obama-Blue.  If the gray value is greater than 60, then the pixel should be changed to Obama-Red. Otherwise the pixel should be Obama-DarkBlue.
## Obama-DarkBlue = makeColor(0,51,76)
## Obama-Red = makeColor(217, 26, 33)
## Obama-Blue = makeColor(112,150,158)
## Obama-Yellow = makeColor(252, 227, 166)
