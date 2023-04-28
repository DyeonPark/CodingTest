import sys

for i in range(int(input())):
  ps = sys.stdin.readline()
  
  stack_cnt = 0
  is_terminated = False
  for j in ps:
    if j == '(':
      stack_cnt += 1
    elif j == ')':
      stack_cnt -= 1

    if stack_cnt < 0:
      is_terminated = True
      break

  if stack_cnt == 0:
    print("YES")
  elif is_terminated:
    print("NO")
  else:
    print("NO")
