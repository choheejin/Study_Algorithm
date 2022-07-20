import sys

N = int(sys.stdin.readline())

array = []
array2 = []
result = []
x_zip =[]

for _ in range(0, N, 1):
  array.append(map(int, sys.stdin.readline().split()))

for x, y in array:
  x_zip.append(x)
  array2.append([x, y])

x_zip = set(x_zip)

for i in x_zip:
  y_zip = []
  for x, y in array2:
    if (i == x):
      y_zip.append(y)
    
  y_zip.sort()
  for y in y_zip:
    print(i, y)

