from PIL import Image,ImageDraw
import random
import math


def dragon(x1,y1,x2,y2,n):
	if n>0:
		x=(x1+x2)/2+(y2-y1)/2
		y=(y1+y2)/2-(x2-x1)/2
		dragon(x2,y2,x,y,n-1)
		dragon(x1,y1,x,y,n-1)
	else:
		draw.line((x1,y1,x2,y2),fill="red")


width=1152
height=864
image = Image.new("RGB",(width,height))
draw=ImageDraw.ImageDraw(image)
dragon(300,400,900,600,20)
image.show()


