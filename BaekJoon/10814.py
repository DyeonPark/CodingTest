# 5m : solved with implementation (sorting) 
import sys

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
mem = []
for i in range(N):
  age, name = input().split()
  mem.append((int(age), name))

mem.sort(key=lambda x: x[0])

for age, name in mem:
  print(age, name)
