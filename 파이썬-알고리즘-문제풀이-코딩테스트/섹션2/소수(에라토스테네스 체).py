# solved : 7m
# 에라토스테네스의 체 : 소수가 아닌 것을 지워나가는 것
import sys
input = sys.stdin.readline

N = int(input())
nums = [1] * (N + 1)
nums[0] = 0
nums[1] = 0

for i in range(2, N):
    j = 2
    while j * i <= N:
        nums[j * i] = 0
        j += 1

print(sum(nums))
