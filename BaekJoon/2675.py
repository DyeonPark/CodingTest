for _ in range(int(input())):
  count, strs = input().split()
  for i in range(len(strs)):
    print(strs[i] * int(count), end='')
  print()
