class AandB():
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def numbers(self):
    array=[0]*(self.b-self.a)
    iterator=0
    if self.a==self.b:
      array.append(self.a)
      return array
    elif self.a>self.b:
      return None
    array.append(self.count(array,self.a,self.b,iterator))
    array.pop()
    return array
  def count(self,array,a,b,iterator):
    if a==self.b:
      return array.append(self.b)
    else:
      array[iterator]=a
      self.a+=1
    return self.count(array,self.a,self.b,iterator+1)


a=AandB(3,10)
print(a.numbers())