import sys

stack = []
for i in range(int(input())):
  cmd = sys.stdin.readline()

  if "push" in cmd:
    cmd, num = cmd.split()
    stack.append(int(num))
  elif "pop" in cmd:
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif "top" in cmd:
    if stack:
      print(stack[-1])
    else:
      print(-1)
  elif "size" in cmd:
    print(len(stack))
  else:  # empty
    if stack:
      print(0)
    else:
      print(1)
