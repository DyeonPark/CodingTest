# 10m : solved with dp
import sys

def input():
  return sys.stdin.readline().rstrip()

fib = [[0, 0] for i in range(41)]
fib[0] = [1, 0]
fib[1] = [0, 1]

for i in range(2, 41):
  fib[i][0] = fib[i - 1][0] + fib[i - 2][0]
  fib[i][1] = fib[i - 1][1] + fib[i - 2][1]

for i in range(int(input())):
  N = int(input())
  print(fib[N][0], fib[N][1])
