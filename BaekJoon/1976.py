# 풀이 링크: https://thinking-developer.tistory.com/167

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
M = int(input())
roots = [i for i in range(N)]

def find(n):
  if roots[n] == n:
    return n
  else:
    root = find(roots[n])
    roots[n] = root
    return roots[n]

def union(i, j):
  root_i = find(i)
  root_j = find(j)

  if root_i == root_j:
    return

  if root_i > root_j:
    roots[root_i] = root_j
  else:
    roots[root_j] = root_i

for i in range(N):
  roads = list(map(int, input().split()))
  ##########################
  for j in range(N):
    if roads[j] == 1:
      union(i, j)
  ##########################

trips = list(map(int, input().split()))
trip_roots = []
for i in trips:
  trip_roots.append(find(i-1))

if l(set(trip_roots)) == 1:
  print("YES")
else:
  print("NO")
