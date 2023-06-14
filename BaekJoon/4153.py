while True:
  lines = list(map(int, input().split()))
  if sum(lines) == 0:
    break
  
  max_l = max(lines)
  lines.remove(max_l)
  
  if max_l ** 2 == sum(list(map(lambda x: x**2, lines))):
    print("right")
  else:
    print("wrong")
