# solved : 15m
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))
maximum = -(sys.maxsize)

# 행의 합 O(N)
for x in range(N):
    total = 0
    for y in range(N):
        total += maps[x][y]
    maximum = max(maximum, total)
    
# 열의 합 O(N)
for y in range(N):
    total = 0
    for x in range(N):
        total += maps[x][y]
    maximum = max(maximum, total)

# 두 대각선의 합 O(2)
for i in [0, N - 1]:
    total = 0
    for j in range(N):
        total += maps[abs(j - i)][j]
    maximum = max(maximum, total)

print(maximum)
