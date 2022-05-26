import sys

N = int(sys.stdin.readline())
cnt = 1
result = 0

while True:
  if N == 0:
    break
  if N < cnt:
    cnt = 1
  result += 1
  N -= cnt
  cnt += 1

print(result)
