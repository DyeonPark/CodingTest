import sys
import heapq

data = []
for i in range(int(input())):
  x = int(sys.stdin.readline())

  if x == 0:
    if data:
      print(heapq.heappop(data)[1])
    else:
      print(0)
  else:
    heapq.heappush(data, (abs(x), x))
