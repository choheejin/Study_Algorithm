import sys

N = int(sys.stdin.readline())
array = []

for _ in range(0, N, 1):
  x, y = map(int, sys.stdin.readline().split())
  array.append([x,y])

array.sort(key=lambda x: (x[1], x[0]))

for x, y in array:
  print(x, y)
