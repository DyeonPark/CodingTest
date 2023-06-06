for _ in range(int(input())):
  H, W, N = map(int, input().split())
  
  if N % H == 0:
    floor = H
    num = (N // H)
  else:
    floor = N % H
    num = (N // H) + 1

  if num < 10:
    print(f"{floor}0{num}")
  else:
    print(f"{floor}{num}")
