import sys

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

result = []
input = sys.stdin.readline().lower()
max_cnt = 0

for i in alpha:
  result.append(input.count(i))
  
max = max(result)

indexList = list(filter(lambda x: result[x] == max, range(len(result))))

if len(indexList) > 1:
  print("?")
else:
  print(alpha[result.index(max)].upper())

