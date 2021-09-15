# 큰 수의 법칙 (전형적인 그리디 알고리즘)
# 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙. 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

# 배열의 크기 : N, 숫자가 더해지는 횟수 : M

# 어떻게 해야할까?

# 숫자가 큰 순서대로 정렬하여 (내림차순 정렬) 가장 큰 수 곱할대로 곱하고 두번째로 큰 수 곱할대로 곱하기 반복

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기 <--- 이 부분 꼭 기억하자!
data = list(map(int, input().split()))

data.sort()

first = data[n - 1]   # 가장 큰 수
second = data[n - 2]  # 두번째로 큰 수

result = 0            # 결과

while True:
  for i in range(k):  # K번 초과하지 않도록 연속 덧셈
    if m == 0:        # m <- 덧셈 횟수
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)
