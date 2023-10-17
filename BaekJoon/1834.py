# 풀이 시간: 3-5m
# 풀이: 수학적 논리 이용 (나머지와 몫)

import sys

def input():
  return sys.stdin.readline().rstrip()

N = int(input())

result = 0
for i in range(1, N):
  result += N * i + i

print(result)
