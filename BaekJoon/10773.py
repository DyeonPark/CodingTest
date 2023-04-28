stack = []

for i in range(int(input())):
  cmd = int(input())
  if cmd == 0:
    stack.pop()
  else:
    stack.append(cmd)

print(sum(stack))
