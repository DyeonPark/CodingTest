from collections import defaultdict

inputs = input().lower()

set_dict = defaultdict(int)
for i in set(inputs):
  set_dict[i] = inputs.count(i)

max_val = max(set_dict.values())
if list(set_dict.values()).count(max_val) > 1:
  print("?")
else:
  print(max(set_dict, key=set_dict.get).upper())
