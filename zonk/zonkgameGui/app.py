from tkinter import *
from tkinter import messagebox
import random
import math

class ZonkGame():
	def __init__(self,root):
		self.canvas = Canvas(root, width=800, height=560,bg="white")
		self.btnExit=Button(text="Exit",
	               command=root.destroy)
		self.btnThrow=Button(text="Throw Bones",
	                command=self.GameStart)
		self.btnExit.place(x=300,y=565)
		self.btnThrow.place(x=400,y=565)
		self.canvas.pack()
		self.total=0
		self.array=list()
		for i in range (random.randint(1,6)):
			self.array.append(random.randint(1,6))
		print (self.array)
	def score(self):
		rule=[1,2,3,4,5,6]
		number=0
		count6dif=0
		count3pair=0
		for x in rule:
			match =0
			for y in self.array:
				if y==x:
					match=match+1
					number=y
			if match==1:
				count6dif+=1
				if count6dif==6:
					self.total=1500
				elif number==5 or number==1:
					if number==5:
						self.total+=50
					elif number==1:
						self.total+=100
			elif match==2:		
				count3pair+=1
				if count3pair==3:
					self.total=750
					continue
				elif number==5 or number==1:
					if number==5:
						self.total+=100
					if number==1:
						self.total+=200
			elif match>=4:
				if number==1:
					self.total+=1000*(match-2)
				else:
					self.total+=number*100*(match-2)
			elif match==3:
				if number==1:
					self.total+=1000
				else:
					self.total+=number*100
		return self.total
	def GameStart(self):
		array=ZonkCount()
		self.canvas.delete("all")
		for i in len(array):
	   	 	number=array[i]
			findDots_and_Painting(i,number)
		if array.score()<=1000:
			messagebox.showwarning("try again",score(array))
		if array.score()>1000:
			messagebox.showinfo("congratulation",score(array))
	def findDots_and_Painting(self,i,number):
	   arrayDotsXStart=[30,293,556]
	   arrayDotsXEnd=[263,526,770]
	   arrayDotsYStart=[50,330]
	   arrayDotsYEnd=[230,530]
	   arrayDotsOfRectangle=list()
	   r=7
	   j=0
	   if i==3:
	      i=0
	      j=1
	   elif i==4:
	      i=1
	      j=1
	   elif i==5:
	      i=2
	      j=1
	   randomNumberX=random.randint(arrayDotsXStart[i],arrayDotsXEnd[i])
	   randomNumberY=random.randint(arrayDotsYStart[j],arrayDotsYEnd[j])
	   arrayDotsOfRectangle.append([randomNumberX-50/2,randomNumberY-50/2])
	   arrayDotsOfRectangle.append([randomNumberX+50/2,randomNumberY-50/2])
	   arrayDotsOfRectangle.append([randomNumberX+50/2,randomNumberY+50/2])
	   arrayDotsOfRectangle.append([randomNumberX-50/2,randomNumberY+50/2])
	   angle=math.radians(random.randint(0,360))
	   cos_val=math.cos(angle)
	   sin_val=math.sin(angle)
	   cx=randomNumberX
	   cy=randomNumberY
	   new_points=[]
	   for x_old,y_old in arrayDotsOfRectangle:
	      x_old-=cx
	      y_old-=cy
	      x_new=x_old*cos_val-y_old*sin_val
	      y_new=x_old*sin_val+y_old*cos_val
	      new_points.append([x_new+cx,y_new+cy])
	   self.canvas.create_polygon(new_points,fill="blue")
	   x=randomNumberX
	   y=randomNumberY
	   x_center=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	   y_center=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	   if number==1:
	      self.canvas.create_oval(x_center-r,y_center-r,x_center+r,y_center+r,fill="white",width=1)
	   elif number==2:
	      x=arrayDotsOfRectangle[0][0]+10
	      y=arrayDotsOfRectangle[0][1]+10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[2][0]-10
	      y=arrayDotsOfRectangle[2][1]-10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	   elif number==3:
	      self.canvas.create_oval(x_center-r,y_center-r,x_center+r,y_center+r,fill="white",width=1)
	      x=arrayDotsOfRectangle[0][0]+10
	      y=arrayDotsOfRectangle[0][1]+10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[2][0]-10
	      y=arrayDotsOfRectangle[2][1]-10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	   elif number==4:
	      x=arrayDotsOfRectangle[0][0]+10
	      y=arrayDotsOfRectangle[0][1]+10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[2][0]-10
	      y=arrayDotsOfRectangle[2][1]-10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[1][0]-10
	      y=arrayDotsOfRectangle[1][1]+10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[3][0]+10
	      y=arrayDotsOfRectangle[3][1]-10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	   elif number==5:
	      self.canvas.create_oval(x_center-r,y_center-r,x_center+r,y_center+r,fill="white",width=1)
	      x=arrayDotsOfRectangle[0][0]+10
	      y=arrayDotsOfRectangle[0][1]+10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[2][0]-10
	      y=arrayDotsOfRectangle[2][1]-10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[1][0]-10
	      y=arrayDotsOfRectangle[1][1]+10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[3][0]+10
	      y=arrayDotsOfRectangle[3][1]-10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	   elif number==6:
	      x=arrayDotsOfRectangle[0][0]+10
	      y=arrayDotsOfRectangle[0][1]+10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[2][0]-10
	      y=arrayDotsOfRectangle[2][1]-10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[1][0]-10
	      y=arrayDotsOfRectangle[1][1]+10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[3][0]+10
	      y=arrayDotsOfRectangle[3][1]-10
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[1][0]-10
	      y=arrayDotsOfRectangle[1][1]+25
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")
	      x=arrayDotsOfRectangle[3][0]+10
	      y=arrayDotsOfRectangle[3][1]-25
	      x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
	      y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
	      self.canvas.create_oval(x_new-r,y_new-r,x_new+r,y_new+r,fill="white")  



root=Tk()
root.title("ZonkGameGui")
root.geometry("800x600")
GUI=ZonkGame(root)
root.mainloop()

"""def GameStart():
	   array=createSet()
	   c.delete("all")
	   for i in range(len(array)):
	     number=array[i]
	     findDots_and_Painting(i,number)
	   if score(array)<=1000:
	      messagebox.showwarning("try again",score(array))
	   if score(array)>1000:
	      messagebox.showinfo("congratulation",score(array))
	screen=Tk()
	screen.title("zonk")
	screen.geometry("800x600")

	btnExit=Button(text="Exit",
	               command=screen.destroy
	              )

	btnThrow=Button(text="Throw Bones",
	                command=GameStart
	              )

	c = Canvas(screen, width=800, height=560,bg="white")
	c.pack()
	btnExit.place(x=300,y=565)
	btnThrow.place(x=400,y=565)
	screen.mainloop()"""
