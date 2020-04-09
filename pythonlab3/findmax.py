class array():
    def __init__(self,array):
        self.array=array
    def prepare(self):
        iterator=0
        return self.findmax(iterator,self.array[0])
    def findmax(self,iterator,number):
        if iterator==len(self.array):
            return number
        elif self.array[iterator]>=number:
            return self.findmax(iterator+1,self.array[iterator])
        else:
            return self.findmax(iterator+1,number)


a=array([23,100,33,4,2,30,45,23])
print(a.prepare())