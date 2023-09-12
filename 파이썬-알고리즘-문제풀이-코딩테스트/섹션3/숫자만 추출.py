# solved: 10m
import sys

def input():
  return sys.stdin.readline().rstrip()

N = input()
num = ""

for n in N:
  if n.isdigit():
    num += n
    
num = int(num)
cnt = 0
for i in range(1, num + 1):
  if num % i == 0:
    cnt += 1

print(num)
print(cnt)
