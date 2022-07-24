import sys

def factorial(N):
  if (N == 0):
    return 1
  else:
    return N * factorial(N-1)


N = int(sys.stdin.readline())

for _ in range(0, N, 1):
  x, y= map(int, sys.stdin.readline().split())
  top = factorial(y)
  bottom = factorial(y - x) * factorial(x)
  print(top//bottom)
