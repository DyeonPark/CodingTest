# solved: 4m
import sys

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
for n in range(N):
  word = input()
  for i, j in zip(word.upper(), word[::-1].upper()):
    if i != j:
      print(f"#{n} NO")
      break
  else:
    print(f"#{n} YES")
