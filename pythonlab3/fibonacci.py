class fibonacci():
  def __init__(self,number):
    self.number=number
    self.a=0
    self.b=1
    self.count=0
  def fibo(self):
    fib =self.a
    if self.count==self.number-2:
      return self.b+self.a
    self.a,self.b=self.b,self.a+self.b
    self.count+=1
    return self.fibo()

a=fibonacci(42)
print(a.fibo())


  


"""def test_fibo():
  passed=0
  if fibonacci(9)==34:
    passed+=1
  if fibonacci(10)==55:
    passed+=1
  if fibonacci(11)==89:
    passed+=1
  if fibonacci(12)==144:
    passed+=1
  if fibonacci(1)==1:
    passed+=1
  if fibonacci(2)==1:
    passed+=1
  if fibonacci(3)==2:
    passed+=1
  if passed==7:
    print("passed")
  else:
    print("nope")
"""