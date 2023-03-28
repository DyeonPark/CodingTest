N, K = map(int, input().split())

coins = [ int(input()) for i in range(N)]

cnt = 0
for coin in coins[::-1]:
  cnt += K // coin
  K -= (K // coin) * coin

print(cnt)
