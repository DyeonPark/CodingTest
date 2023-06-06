import string

strs = input()
lc = string.ascii_lowercase

for i in lc:
  if i in strs:
    print(strs.index(i), end = " ")
  else:
    print("-1", end = " ")
