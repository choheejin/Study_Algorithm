A, B, C = map(int, input().split())

for i in range(C):
    A ^= B

print(A)