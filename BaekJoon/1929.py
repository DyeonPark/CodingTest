MAX = 1000000
M, N = map(int, input().split())
is_prime_list = [True] * (MAX + 1)

# 작은 수부터 해당 수의 배수들을 False 처리
for i in range(2, (MAX + 1) // 2):
  j = 2
  while i * j <= MAX:
    is_prime_list[i*j] = False
    j += 1

# 남아있는 수(소수)만 출력
for i in range(M, N + 1):
  if is_prime_list[i]:
    print(i)
