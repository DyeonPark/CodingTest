# 소요시간: 측정하지 않음
# 참고 여부: 방법 1은 풀이 방법만 참고 / 방법 2는 코드도 참고
# 풀이 이미지: https://media.discordapp.net/attachments/1018477653860294689/1160946787452997663/image.png?ex=653682f3&is=65240df3&hm=dae5f07059a0ac52e58a5465ade30e0338c0a75c9526cff9f8b5e599679be830&=&width=1056&height=1365

# 방법1: 2차원 배열 사용 -> 메모리 초과
import sys

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
dp = [[0] * N for i in range(N)]

for _ in range(1, N):
  i = (N - 1) - _
  j = 4
  while i >= 0:
    if abs(j - i) == 1:
      dp[i][j] = 1
    else:
      if arr[i] == arr[j]:
        dp[i][j] = dp[i + 1][j - 1]
      else:
        dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

    i -= 1
    j -= 1

print(dp[0][-1])

# 방법2: 메모리를 절약하기 위해, 행 인덱스가 홀/짝임에 따라서 (2xN) 크기의 배열을 사용
import sys

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
dp = [[0] * N for i in range(N)]

for _ in range(1, N):
  i = (N - 1) - _
  j = 4
  while i >= 0:
    if abs(j - i) == 1:
      dp[i][j] = 1
    else:
      if arr[i] == arr[j]:
        dp[i][j] = dp[i + 1][j - 1]
      else:
        dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

    i -= 1
    j -= 1

print(dp[0][-1])
