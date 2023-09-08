# 생각 및 풀이 시도 -> 실패 : 31m 
# 다른 사람의 풀이 참고 : 16m
# 다른 사람의 풀이 토대로 작성 및 오류 해결 : 32m
# 총 약 1시간 20분 소요
# 참고 링크: https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2636-%EC%B9%98%EC%A6%88-BFS

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]

cheese = [sum([sum(plate[i])for i in range(N)])]
time = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 탐색 방법
# 큐에 현재 방문한 노드와 이어진, 즉 다음으로 방문할 노드를 넣는다 (이미 방문한 노드라면 넣지 않는다)
# 다음으로 이동할 노드는 큐의 head에서 갖고 온다
# 모든 노드를 방문하여 더이상 갈 곳이 없을 때 까지(큐가 빌 때까지)반복한다

def bfs(time):
  q = deque([(0, 0)])
  melt = deque([])
  visited = [[0] * M for _ in range(N)] # 방문기록은 매번 다시 트래킹해야 함
  
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 판을 벗어나지 않게 하고, 방문하지 않은 것만 방문하게 하는 if문
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        visited[nx][ny] = 1 # 방문처리
        if plate[nx][ny] == 0: # 공기면 이동할 노드로써 큐에 삽입
          q.append((nx, ny))
        else: # 치즈면 녹일 리스트에 추가
          melt.append((nx, ny))

  for x, y in melt: # 한 번에 녹이기
    plate[x][y] = 0
    
  time += 1
  return len(melt), time

while cheese[-1] > 0:
  new_melted, time = bfs(time)
  cheese.append(cheese[-1] - new_melted)

print(time)
print(cheese[-2])
