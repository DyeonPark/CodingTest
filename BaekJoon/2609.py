N, M = map(int, input().split())

for i in range(min(N, M) + 1, 0, -1):
  if N % i == 0 and M % i == 0:
    print(i)
    print(i * (N // i) * (M // i))
    break
