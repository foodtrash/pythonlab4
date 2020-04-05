from PIL import Image
import math
iterator=80
z=0
n=0

RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

def mandelbrot(c,z,n):
	if abs(z)<=2 and n<iterator:
		c=c
		mandelbrot(c,z*z+c,n+1)
	else:
		return

c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
            IM_START + (y / HEIGHT) * (IM_END - IM_START))


mandelbrot(c,z,n)

width=1024
height=768
img = Image.new("RGB",(width,height))
draw=img.load()
