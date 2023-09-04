# solved : 8m
import sys

for i in range(int(input())):
    N, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    print(f"#{i + 1} {sorted(nums[s - 1: e])[k - 1]}")
