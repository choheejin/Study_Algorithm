import sys

N = int(sys.stdin.readline())
dict = []

for _ in range(0, N, 1):
  word = sys.stdin.readline().strip() 
  dict.append((len(word), word))

dict = set(dict)
dict = sorted(dict, key = lambda x : (x[0], x[1]))

for word in dict:
  print(word[1])
