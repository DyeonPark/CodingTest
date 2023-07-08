N = 20
dp = [[[[None] for _ in range(N+1)] 
       for _ in range(N+1)] 
      for _ in range(N+1)
     ]

def recur(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
    if dp[0][0][0][0] is None:
      dp[0][0][0][0] = 1
    return dp[0][0][0][0]
  elif a > 20 or b > 20 or c > 20:
    if dp[20][20][20][0] is None:
      dp[20][20][20][0] = recur(20, 20, 20)
    return dp[20][20][20][0]
  elif a < b and b < c:
    if dp[a][b][c][0] is None:
      dp[a][b][c][0] = recur(a, b, c-1) + recur(a, b-1, c-1) - recur(a, b-1, c)
    return dp[a][b][c][0]
  else:
    if dp[a][b][c][0] is None:
      dp[a][b][c][0] = recur(a-1, b, c) + recur(a-1, b-1, c) + recur(a-1, b, c-1) - recur(a-1, b-1, c-1)
    return dp[a][b][c][0]

while True:
  a, b, c = map(int, input().split())
  if a == -1 and b == -1 and c == -1:
    break
    
  print(f"w({a}, {b}, {c}) = {recur(a, b, c)}")
