while True:
  strs = input()
  if strs == '0':
    break 

  is_pd = True
  for i in range(len(strs)//2):
    if strs[i] != strs[-(i+1)]:
      print("no")
      is_pd = False
      break

  if is_pd:
    print("yes")
