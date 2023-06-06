H, M = map(int, input().split())

time = (H * 60 + M) - 45

if time < 0:
  time = 1440 + time

H = time // 60
M = time - (H * 60)
print(f"{H} {M}")
