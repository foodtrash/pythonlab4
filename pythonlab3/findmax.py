def findmax(array,n):
  if n==1:
    return array[0]
  return max(array[n-1],findmax(array,n-1))


array=[1,4,45,6,200,10,3,4]
n=len(array)
print(findmax(array,n))
