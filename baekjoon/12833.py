A, B, C = map(int, input().split())

for i in range(C%2):
    A ^= B

print(A)

# XOR 연산은 두 피연산자의 bit 가 다르면 1, 같으면 0
# n번째 결과는 n+2번째 결과와 같음
# 01 ^ 11 => 10 ^ 11 => 01 ^ 11 ...