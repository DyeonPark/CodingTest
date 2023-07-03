N = int(input())
col = [0] * (N)
ans = 0

def promising(x): # 가지가 유망한지를 판단
  for i in range(x):
    # 같은 열에 있는 경우 or 대각선에 있는 경우
    if col[x] == col[i] or abs(col[x] - col[i]) == abs(x - i):
      return False
  return True

def n_queens(x):
  global ans
  if N == x: # 가지가 끝까지 도달한 경우
    ans += 1
    return
  else: # 가지가 더 내려갈 수 있는 경우
    for i in range(N): # 가지 경우의 수를 차례로 탐색
      col[x] = i
      if promising(x): # 방금 놓은 수(가지)가 유망한 경우
        n_queens(x + 1)

n_queens(0)
print(ans)
