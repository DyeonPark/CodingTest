# solved: 10m
import sys

def input():
  return sys.stdin.readline().rstrip()

N = input()
num = ""
# num = 0  # 답안 풀이

for n in N:
  # 답안에서는 n.isdecimal()을 사용
  # isdigit() : 숫자처럼 생긴 특수문자도 True를 내뱉음
  # isdecimal() : int형으로 변환 가능한 것에만 True를 내뱉음 (즉, 특수문자로 된 숫자는 False가 나옴)
  if n.isdigit():
    num += n
    # num = num * 10 + int(n)  # 답안 풀이
    
num = int(num)
cnt = 0
for i in range(1, num + 1):
  if num % i == 0:
    cnt += 1

print(num)
print(cnt)
