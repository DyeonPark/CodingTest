import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M, V = map(int, input().split())

# 그래프 입력
graph = [[] for i in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b) # 무방향 그래프이기 때문에 
  graph[b].append(a) # a->b, b->a 둘 다 해줘야 함


# Stack 자료구조를 이용 (함수 호출이 이미 stack 구조)
def dfs(v, visited):
  visited[v] = 1 # 방문처리
  print(v, end=' ')

  for i in sorted(graph[v]):
    if not visited[i]:
      dfs(i, visited)

# Queue 자료구조를 이용
def bfs(v, visited):
  queue = deque([v])
  visited[v] = 1
  
  while queue:
    node = queue.popleft()
    print(node, end=' ')
    
    for i in sorted(graph[node]):
      if not visited[i]:
        queue.append(i)
        visited[i] = 1 # 방문처리를 하는 위치에 주의


def graph_search(v: int, mode: str):
  visited = [0] * (N + 1)
  visited[0] = 1

  if mode == "dfs":
    dfs(v, visited)
  else:
    bfs(v, visited)


graph_search(V, "dfs")
print()
graph_search(V, "bfs")
