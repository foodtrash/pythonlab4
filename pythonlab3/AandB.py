class AandB():
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def numbers(self):
    array=[0]*(self.b-self.a)
    iterator=0
    start=self.a
    if self.a==self.b:
      array.append(self.a)
      return array
    elif self.a>self.b:
      return None
    array.append(self.count(array,start,self.b,iterator))
    array.pop()
    return array
  def count(self,array,a,b,iterator):
    if a==self.b:
      return array.append(self.b)
    else:
      array[iterator]=a
    return self.count(array,a+1,self.b,iterator+1)

a=AandB(10,13)
print(a.numbers())
"""def test_numbers():
  z=0
  if numbers(4,10)==[4,5,6,7,8,9,10]:
    z+=1
  if numbers(10,20)==[10,11,12,13,14,15,16,17,18,19,20]:
    z+=1
  if numbers(10,10)==[10]:
    z+=1
  if numbers(3,2)==None:
    z+=1
  if z==4:
    print("passed")"""
