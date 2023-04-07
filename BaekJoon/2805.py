import sys

N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(trees)

while start <= end:

  mid = (start + end) // 2
  cutted = sum([i - mid for i in trees if i > mid])

  if cutted >= M:
    start = mid + 1
  else: # cutted < M
    end = mid -1
    
print(end)
    
