# 숫자 카드 게임

# 1. 숫자가 쓰인 카드들은 N * M 형태로 놓여 있다. 이때, N은 행의 갯수, M은 열의 갯수
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
# 3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 4. 따라서, 처음에 골라낼 행을 선택할때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야한다.

# Think -> 행마다의 가장 작은 수 비교하여 가장 큰 수가 있는 행 선택.

# min() 함수 이용

n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_data = min(data)
  result = max(result, min_data)

print(result)

# 2중 반복문 이용

n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_data = 10001
  for a in data:
    min_data = min(min_data, a)
  result = max(result, min_data)

print(result)