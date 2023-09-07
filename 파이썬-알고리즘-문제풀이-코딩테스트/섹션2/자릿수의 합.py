# sovled : 3m
import sys
input = sys.stdin.readline

def digit_sum(x):
    total = 0
    for i in str(x):
        total += int(i)
    return total

N = int(input())
nums = list(map(int, input().split()))

res = []
for num in nums:
    res.append(digit_sum(num))

print(nums[res.index(max(res))])
