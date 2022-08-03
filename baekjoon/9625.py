import sys

K = int(sys.stdin.readline())
array = ['a']

for _ in range(K):
  cnt = 0
  i = 0
  num = len(array)
  while cnt != num:
    if(array[i] == 'b'):
      array.insert(i+1, 'a')
      i = i + 2
    else:
      array.pop(i)
      array.insert(i, 'b')
      i = i + 1
    cnt = cnt + 1

print(array.count('a'), end='')
print(array.count('b'))
  
