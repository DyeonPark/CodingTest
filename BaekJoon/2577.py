A = int(input())
B = int(input())
C = int(input())

num = str(A * B * C)
for i in range(0, 10):
  print(num.count(str(i)))
