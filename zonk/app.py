from tkinter import *
from tkinter import messagebox
import random
import math
from zonk import *

class ZonkGame():
    def __init__(self,root=None):
        self.sys=root

    def Buttons(self):
        #buttons to gui
        self.canvas = Canvas(self.sys, width=800, height=560,bg="white")
        self.btnExit=Button(text="Exit",
                   command=self.sys.destroy)
        self.btnThrow=Button(text="Throw Bones",
                   command=self.GameStart)
        self.btnExit.place(x=300,y=565)
        self.btnThrow.place(x=400,y=565)
        self.canvas.pack()

    def GameStart(self):
        self.canvas.delete("all")
        self.total=0
        #create total
        self.array=list()
        for i in range (random.randint(1,6)):
            self.array.append(random.randint(1,6))

        for number in range(len(self.array)):
            self.findDots(self.array[number],number)
        if self.score()<=1000:
            messagebox.showwarning("try again",self.score())
        if self.score()>1000:
            messagebox.showwarning("congratulations",self.score())
        print(self.array)
        print(self.score())

    def score(self,set=None):
        #find score of set
        rule=[1,2,3,4,5,6]
        total=0
        number=0
        if set!=None:
            array=set
        else:
            array=self.array
        count6dif=0
        count3pair=0
        for x in rule:
            match=0
            for y in array:
                if y==x:
                    match=match+1
                    number=y
            if match==1:
                count6dif+=1
                if count6dif==6:
                    total=1500
                elif number==5 or number==1:
                    if number==5:
                        total+=50
                    elif number==1:
                        total+=100
            elif match==2:      
                count3pair+=1
                if count3pair==3:
                    total=750
                    continue
                elif number==5 or number==1:
                    if number==5:
                        total+=100
                    if number==1:
                        total+=200
            elif match>=4:
                if number==1:
                    total+=1000*(match-2)
                else:
                    total+=number*100*(match-2)
            elif match==3:
                if number==1:
                    total+=1000
                else:
                    total+=number*100
        return total

    def findDots(self,number,count):
        #find dots for rectangle
        arrayDotsXStart=[30,293,556]
        arrayDotsXEnd=[263,526,770]
        arrayDotsYStart=[50,330]
        arrayDotsYEnd=[230,530]
        arrayDotsOfRectangle=list()
        j=0
        if count==3:
            count=0
            j=1
        elif count==4:
            count=1
            j=1
        elif count==5:
            count=2
            j=1
        randomNumberX=random.randint(arrayDotsXStart[count],arrayDotsXEnd[count])
        randomNumberY=random.randint(arrayDotsYStart[j],arrayDotsYEnd[j])
        arrayDotsOfRectangle.append([randomNumberX-50/2,randomNumberY-50/2])
        arrayDotsOfRectangle.append([randomNumberX+50/2,randomNumberY-50/2])
        arrayDotsOfRectangle.append([randomNumberX+50/2,randomNumberY+50/2])
        arrayDotsOfRectangle.append([randomNumberX-50/2,randomNumberY+50/2])
        x=randomNumberX
        y=randomNumberY

        #rotate rectangle of 360 
        angle=math.radians(random.randint(0,360))
        cos_val=math.cos(angle)
        sin_val=math.sin(angle)
        cx=randomNumberX
        cy=randomNumberY

        #new array of rotating rectangle
        new_points=[]
        for x_old,y_old in arrayDotsOfRectangle:
            x_old-=cx
            y_old-=cy
            x_new=x_old*cos_val-y_old*sin_val
            y_new=x_old*sin_val+y_old*cos_val
            new_points.append([x_new+cx,y_new+cy])
        self.painting(new_points,x,y,randomNumberX,randomNumberY,angle,arrayDotsOfRectangle,number)

    def painting(self,new_points,x,y,randomNumberX,randomNumberY,angle,arrayDotsOfRectangle,number):
        
        #radius of circle
        radius=7

        #create poligon by start positions of rectangle 
        self.canvas.create_polygon(new_points,fill="blue")

        #paint circles inside rectangle
        x_center=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
        y_center=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
        if number==1 or number==3 or number==5:
            self.canvas.create_oval(x_center-radius,y_center-radius,x_center+radius,y_center+radius,fill="white",width=1)

        if number==2 or number==3:
            x=arrayDotsOfRectangle[0][0]+10
            y=arrayDotsOfRectangle[0][1]+10
            x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
            y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
            self.canvas.create_oval(x_new-radius,y_new-radius,x_new+radius,y_new+radius,fill="white")
            x=arrayDotsOfRectangle[2][0]-10
            y=arrayDotsOfRectangle[2][1]-10
            x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
            y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
            self.canvas.create_oval(x_new-radius,y_new-radius,x_new+radius,y_new+radius,fill="white")

        if number==4 or number==5 or number==6:
            x=arrayDotsOfRectangle[0][0]+10
            y=arrayDotsOfRectangle[0][1]+10
            x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
            y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
            self.canvas.create_oval(x_new-radius,y_new-radius,x_new+radius,y_new+radius,fill="white")
            x=arrayDotsOfRectangle[1][0]-10
            y=arrayDotsOfRectangle[1][1]+10
            x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
            y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
            self.canvas.create_oval(x_new-radius,y_new-radius,x_new+radius,y_new+radius,fill="white")
            x=arrayDotsOfRectangle[2][0]-10
            y=arrayDotsOfRectangle[2][1]-10
            x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
            y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
            self.canvas.create_oval(x_new-radius,y_new-radius,x_new+radius,y_new+radius,fill="white")
            x=arrayDotsOfRectangle[3][0]+10
            y=arrayDotsOfRectangle[3][1]-10
            x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
            y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
            self.canvas.create_oval(x_new-radius,y_new-radius,x_new+radius,y_new+radius,fill="white")

        if number==6:
            x=arrayDotsOfRectangle[1][0]-10
            y=arrayDotsOfRectangle[1][1]+25
            x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
            y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
            self.canvas.create_oval(x_new-radius,y_new-radius,x_new+radius,y_new+radius,fill="white")
            x=arrayDotsOfRectangle[3][0]+10
            y=arrayDotsOfRectangle[3][1]-25
            x_new=math.cos(angle)*(x-randomNumberX)-math.sin(angle)*(y-randomNumberY)+randomNumberX
            y_new=math.sin(angle)*(x-randomNumberX)+math.cos(angle)*(y-randomNumberY)+randomNumberY
            self.canvas.create_oval(x_new-radius,y_new-radius,x_new+radius,y_new+radius,fill="white")  


if __name__=="__main__":
    root=Tk()
    root.title("ZonkGameGui")
    root.geometry("800x600")
    GUI=ZonkGame(root)
    GUI.Buttons()
    root.mainloop()


