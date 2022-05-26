import sys

N = int(sys.stdin.readline())
input = map(int, sys.stdin.readline().split())
list = sorted(input)

sum = 0

for i in list:
  sum += i

avg = sum / N
result = avg / list[N-1] * 100

print(result)
