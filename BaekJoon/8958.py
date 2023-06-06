for _ in range(int(input())):
  ans = input()
  res = [0] * len(ans)
  
  for idx in range(len(ans)):
    if ans[idx] == "O":
      if ans[idx-1] == "O" and idx >0:
        res[idx] = res[idx-1] + 1
      else:
        res[idx] = 1
    else:
      res[idx] = 0

  print(sum(res))
