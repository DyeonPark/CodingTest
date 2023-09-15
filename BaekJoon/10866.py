# 15m : solved with implementation
import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

class Deque:
  def __init__(self):
    self.nums = deque([])

  def prompt(self, cmd):
    if cmd[0] == "size":
      print(len(self.nums))
      
    elif cmd[0] == "empty":
      print(self.is_empty())
      
    elif cmd[0] == "front":
      if self.is_empty():
        print(-1)
      else:
        print(self.nums[0])
        
    elif cmd[0] == "back":
      if self.is_empty():
        print(-1)
      else:
        print(self.nums[-1])
        
    elif cmd[0] == "push_front":
      self.nums.appendleft(int(cmd[1]))
      
    elif cmd[0] == "push_back":
      self.nums.append(int(cmd[1]))
      
    elif cmd[0] == "pop_front":
      if self.is_empty():
        print(-1)
      else:
        print(self.nums.popleft())
        
    elif cmd[0] == "pop_back":
      if self.is_empty():
        print(-1)
      else:
        print(self.nums.pop())

    elif cmd[0] == "nums":
      print(self.nums)

  def is_empty(self):
    if len(self.nums) == 0:
      return 1
    else:
      return 0

dq = Deque()
for _ in range(int(input())):
  cmd = list(input().split())
  dq.prompt(cmd)
