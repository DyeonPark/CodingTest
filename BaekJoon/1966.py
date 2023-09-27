import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  queue = list(map(int, input().split()))
  print_queue = deque([(queue[i], True) if i == M else (queue[i], False) for i in range(N)])

  print_cnt = 0
  while print_queue:
    top = print_queue.popleft()
    if print_queue and max(print_queue, key=lambda x: x[0])[0] > top[0]:
      print_queue.append(top)
    else:
      print_cnt += 1
      if top[1]:
        print(print_cnt)
        break
