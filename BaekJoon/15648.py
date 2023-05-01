from itertools import permutations

N, M = map(int, input().split())

for i in permutations(list(range(1, N+1, 1)), M):
  print(" ".join([str(j) for j in i]))
