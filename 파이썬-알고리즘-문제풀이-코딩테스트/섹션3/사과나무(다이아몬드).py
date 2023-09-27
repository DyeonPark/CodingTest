# solved : 40m
# 문제의 난이도 자체가 높은 것은 아니었지만, 탐색을 어떻게 효율적으로 할지 하다가 로직이 많이 꼬여서 오래걸림
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
trees = []
for _ in range(N):
    trees.append(list(map(int, input().split())))
    
half = N // 2
total = 0

for y in range(half): # O(N/2) - 열 단위로 접근
    for bias in range(-y, y+1):
        total += trees[half + bias][y]

for y in range(half, N): # O(N/2) - 열 단위로 접근
    for bias in range(-(N - y - 1), N - y):
        total += trees[half + bias][y]

print(total)
