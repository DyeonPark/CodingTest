from collections import Counter

N = int(input())
arr_list = list(map(int, input().split()))
arr_set = set(arr_list)

M = int(input())
find_list = list(map(int, input().split()))

counted = Counter(arr_list)

result = []
for i in find_list:
  if i in arr_set:
    result.append(str(counted[i]))
  else:
    result.append(str(0))

print(' '.join(result))
