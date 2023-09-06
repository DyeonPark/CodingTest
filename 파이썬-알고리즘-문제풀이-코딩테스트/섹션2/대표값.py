# solved : 8m
import sys
import math
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
mean = round(sum(scores) / N)

diff = []
for i in scores:
    diff.append(abs(i - mean))

minimum = min(diff)
res = []
for i in range(N):
    if diff[i] == minimum:
        res.append(scores[i])

maximum = max(res)
print(mean, scores.index(maximum) + 1)
