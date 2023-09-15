# 5m : solved with implementation 
import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

nums = deque([])
for _ in range(int(input())):
  cmds = list(input().split())
  if cmds[0] == "push":
    nums.append(int(cmds[1]))
  elif cmds[0] == "pop":
    if len(nums) > 0:
      print(nums.popleft())
    else:
      print(-1)
  elif cmds[0] == "size":
    print(len(nums))
  elif cmds[0] == "empty":
    if len(nums) == 0:
      print(1)
    else:
      print(0)
  elif cmds[0] == "front":
    if len(nums) > 0:
      print(nums[0])
    else:
      print(-1)
  elif cmds[0] == "back":
    if len(nums) > 0:
      print(nums[-1])
    else:
      print(-1)
