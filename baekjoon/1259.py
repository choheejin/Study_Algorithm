import sys

while True:
  N = sys.stdin.readline().strip()
  if(N == '0'):
    break
  if(N == N[::-1]):
    print('yes')
  else:
    print('no')
