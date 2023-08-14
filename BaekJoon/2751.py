# 풀이 포스트 링크: https://thinking-developer.tistory.com/163
# 첫 번째 풀이 (내장 sort 이용)
import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(int(input()))]

for i in sorted(nums):
  print(i)

# 두 번째 풀이 (defaultdict를 이용한 counting sort)
import sys
from collections import defaultdict

input = sys.stdin.readline
nums = defaultdict(int)

for _ in range(int(input())):
  nums[int(input())] += 1

for i in sorted(nums.keys()):
  print(i * nums[i], end='\n')
