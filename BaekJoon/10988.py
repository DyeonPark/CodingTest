# 풀이 포스트 링크: https://thinking-developer.tistory.com/162
# 나의 풀이
s = input()
is_pallen = True

for i in range(len(s)//2):
  if s[i] != s[-(i+1)]:
    is_pallen = False 
    break

if is_pallen:
  print(1)
else:
  print(0)

# 다른 풀이 (좀 더 간단하다!)
s = input()

if s[::-1] == s:
    print(1)
else:
    print(0)
