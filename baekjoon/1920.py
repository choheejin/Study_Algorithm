import sys

N = int(sys.stdin.readline())
N_array = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_array = list(map(int, sys.stdin.readline().split()))


for i in M_array:
  if(i in N_array):
    print(1)
  else:
    print(0)
