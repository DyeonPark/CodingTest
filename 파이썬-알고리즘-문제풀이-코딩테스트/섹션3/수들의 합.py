import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
# 60점 (2문제는 시간초과)
for i in range(N):
    for j in range(i, N):
        if sum(nums[i:j + 1]) == M:
            cnt += 1
            break
        
print(cnt)
