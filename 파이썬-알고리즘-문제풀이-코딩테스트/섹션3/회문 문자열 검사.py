# solved : 4m
import sys

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
for n in range(1, N + 1):
  word = input()
  # if word.uppper() == word[::-1].upper(): # 이와 같은 형태로 비교할 수도 있음 (시간복잡도는 동일)
  for i, j in zip(word.upper(), word[::-1].upper()): # 이 for문은 절반만 돌도록 수정해도 좋음
    if i != j:
      print(f"#{n} NO")
      break
  else:
    print(f"#{n} YES")
