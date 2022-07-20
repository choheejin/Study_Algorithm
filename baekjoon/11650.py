import sys

N = int(sys.stdin.readline())

array = []


for _ in range(0, N, 1):
  a, b = map(int, sys.stdin.readline().split())
  array.append([a, b])

array.sort()

for x, y in array:
  print(x, y)
