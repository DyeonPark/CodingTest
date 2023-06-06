answer = [i for i in range(1, 9)]
nums = list(map(int, input().split()))

if answer == nums:
  print("ascending")
elif sorted(answer, reverse=True) == nums:
  print("descending")
else:
  print("mixed")
