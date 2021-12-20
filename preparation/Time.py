# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초 까지의 모든 시각중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각안에 '3'이 포함되어 있다면 카운드 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1
print(count)