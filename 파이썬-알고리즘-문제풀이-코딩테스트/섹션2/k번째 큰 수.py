# solved : 4m
import sys
from itertools import combinations

N, K = map(int, input().split())
nums = list(map(int, input().split()))

# res = []
res = set()
for comb in combinations(nums, 3):
    # res.append(sum(comb))
    res.add(sum(comb))

# print(sorted(list(set(res)), reverse=True)[K - 1])
print(sorted(list(res), reverse=True)[K - 1])
