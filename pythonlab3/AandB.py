
def numbers(a,b):
  array=[0]*(b-a)
  iterator=0
  if a==b:
    array.append(a)
    return array
  elif a>b:
    return None
  elif b<a:
    return None
  array.append(count(array,a,b,iterator))
  array.pop()
  return array

def count(array,a,b,iterator):
  if a==b:
    array.append(b)
  else:
    array[iterator]=a
    return count(array,a+1,b,iterator+1)


"""def number(a,b):
  if a>b:
    return None
  if a<0:
    return None
  print(a)
  return number(a+1,b)"""

def test_numbers():
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
    print("passed")
