import math
import random
from PIL import Image,ImageDraw

x=2000
y=1080

def petalR(x,y,c,n=1):
	if n==30-c:
		return
	else:
		xe=x+4*n
		ye=y-1*n
		draw.line((x,y,xe,ye),fill="green")
	return petalR(xe,ye,c,n+1)

def petalL(x,y,c,n=1):
	if n==30-c:
		return
	else:
		xe=x-3*n
		ye=y-1*n
		draw.line((x,y,xe,ye),fill="green")
	return petalL(xe,ye,c,n+1)


def paint(x,y,n=30,c=1):
	if n==4:
		return
	else:
		xe=x+1*n
		ye=y-2*n
		draw.line((x,y,xe,ye),fill="green")
		if n%2==0:
			petalR(x,y,c)
		if n%2==1:
			petalL(xe,ye,c)

	return paint(xe,ye,n-1,c+1)


image=Image.new("RGB",(4000,1080),(0,0,0))
draw=ImageDraw.ImageDraw(image)
paint(x,y)
image.show()
