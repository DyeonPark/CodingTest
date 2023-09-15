# 3m : solved with implementation (using math lib)
import sys
import math

def input():
  return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
print(math.comb(N, K))
