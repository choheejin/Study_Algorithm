import sys

def factorial(N):
  if(N==0):
    return 1
  return N * factorial(N-1)

N = int(sys.stdin.readline())
cnt = 0

facNum = str(factorial(N))

for i in range(len(facNum)-1, 0, -1):
  if( facNum[i] == '0' ):
    cnt = cnt + 1
  if( facNum[i-1] != '0'):
    break

print(cnt)
