# 1이 될 때까지 (최소 횟수)
# n 이 1이 될때까지 두가지 연산 반복 (1. N에서 1을 뺀다 2. n을 k로 나눈다 ) 단, 2의 연산은 n 이 k로 나누어 떨어질때 가능하다.

n, k = map(int, input().split())
result = 0

# n 이 k 이상일때 k로 나누기
while n >= k:
  # n 이 k 로 나누어 떨어질때까지 1 빼기
  while n % k != 0:
    n -= 1
    result += 1
  n //= k
  result += 1

# 남은 n에 대해서 1 빼기
while n > 1:
  n -= 1
  result += 1

print(result)