# 거스름돈(N원) 최소 동전 구하기

# 500, 100, 50, 10 원
# 가장 큰 화폐 단위부터 거슬러줘야 함.

n = int(input("거스름돈은 얼마인가? "))
coin_type = [500, 100, 50, 10]

count = 0

for coin in coin_type:
  count += n // coin
  n %= coin

print(count)