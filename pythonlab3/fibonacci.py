class fibonacci():
  def __init__(self,number):
    self.number=number
    self.a=0
    self.b=1
    self.count=0
  def fibo(self):
    if self.number==0:
      return self.a
    if self.number==1:
      return self.b
    fib =self.a
    if self.count==self.number-2:
      return self.b+self.a
    self.a,self.b=self.b,self.a+self.b
    self.count+=1
    return self.fibo()
