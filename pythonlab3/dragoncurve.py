from PIL import Image,ImageDraw
import random
import math

class CurveDragon():
    def __init__(self,n):
        self.image=Image.new("RGB",(1024,768))
        self.draw=ImageDraw.ImageDraw(self.image)
        self.n=n
    def Drawing(self):
        x1=300
        x2=900
        y1=400
        y2=600
        n=self.n
        self.dragon(x1,y1,x2,y2,n)
        self.image.show()
    def dragon(self,x1,y1,x2,y2,n):
    	if n>0:
            x=(x1+x2)/2+(y2-y1)/2
            y=(y1+y2)/2-(x2-x1)/2
            self.dragon(x2,y2,x,y,n-1)
            self.dragon(x1,y1,x,y,n-1)
    	else:
    		self.draw.line((x1,y1,x2,y2),fill="red")

a=CurveDragon(20)
a.Drawing()