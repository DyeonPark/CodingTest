import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
nums = [i for i in range(N + 1)]


def find(n):
  if nums[n] == n:
    return n
  else:
    root = find(nums[n])
    nums[n] = root
    return nums[n]


def union(a, b):
  root_a = find(a)
  root_b = find(b)
  if root_a == root_b:
    return

  if root_a > root_b:
    nums[root_a] = root_b
		# nums[a] = root_b # 틀린 코드
  else:
    nums[root_b] = root_a
		# nums[b] = root_a # 틀린 코드


def is_union(a, b):
  return find(a) == find(b)


for _ in range(M):
  cmd, a, b = map(int, input().rstrip().split())

  if cmd:
    if is_union(a, b):
      print("YES")
    else:
      print("NO")
  else:
    union(a, b)
