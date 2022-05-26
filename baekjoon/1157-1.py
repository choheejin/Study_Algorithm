import sys

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

result = []
input = sys.stdin.readline().lower()
max_cnt = 0

for i in alpha:
  result.append(input.count(i))
  
max = max(result)

for x in result:
  if max == x:
    max_cnt += 1


if max_cnt > 1:
  print("?")
else:
  print(alpha[result.index(max)].upper())
  
