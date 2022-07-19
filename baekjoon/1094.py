import sys

def divide(array, X):
  array.sort()
  temp = array.pop(0) // 2
  array.insert(0, temp)
  
  if(X > sum(array)):
    array.insert(0, temp)

array = []
X = int(sys.stdin.readline())
array.append(64)


while True:
  num = sum(array)
  if(X == num):
    break;
  else:
    divide(array, X)

print(len(array))
