def build(left, right, node):
  if left == right:
    trees[node] = nums[left]
    trees_pos[left] = node
    return trees[node]
  else:
    mid = (left + right) // 2
    trees[node] = build(left, mid, node * 2) + build(mid + 1, right, node * 2 + 1)
    return trees[node]

def query(left, right, start, end, node):
  if right < start or end < left:
    return 0
  elif start <= left and right <= end:
    return trees[node]
  else:
    mid = (left + right) // 2
    return query(left, mid, start, end, node * 2) + query(mid + 1, right, start, end, node * 2 + 1)
    
def update(val, node, new_val):
  diff = new_val - val
  while node > 0:
    trees[node] += diff
    node //= 2
    
N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

trees = [0] * (4 * N)
trees_pos = [0] * N

build(0, N - 1, 1) # initialize tree

for _ in range(M + K):
  a, b, c = map(int, input().split())

  if a == 1:  # chagne
    update(nums[b - 1], trees_pos[b - 1], c)
    nums[b - 1] = c
  else:  # sum of partition
    print(query(0, N - 1, b - 1, c - 1, 1))
