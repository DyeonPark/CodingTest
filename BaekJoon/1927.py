import heapq
import sys

hq = []
for i in range(int(input())):
  x = int(sys.stdin.readline())
  if x == 0:
    if hq:
      print(heapq.heappop(hq))
    else:
      print(0)
  else:
    heapq.heappush(hq, x)
