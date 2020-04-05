def fibonacci(number):
  if number<0:
    print("error")
  elif number==0:
    return 0
  elif number==1:
    return 1
  elif number==2:
    return 1
  else:
    return fibonacci(number-1)+fibonacci(number-2)
  


def test_fibo():
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
