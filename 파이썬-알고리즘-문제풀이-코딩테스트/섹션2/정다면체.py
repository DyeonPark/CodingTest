# solved : 21m
# 전체 코드 시간복잡도 : O(N^2 * M)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sum_list = []
cnt = []

# O(N*M)
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sum_list.append(i + j)

# O(N^2 * M)
for i in sum_list: # O(N*M)
    cnt.append(sum_list.count(i)) # O(N)
    
maximum = max(cnt) # O(N)

res = set()
# O(N*M)
for idx, count in enumerate(cnt):
    if count == maximum:
        res.add(sum_list[idx])

# O(NlogN)
for i in sorted(list(res)):
    print(i, end=' ')


# 강사 풀이 : 가능한 합을 카운팅하는 방식으로 했는데, 이게 훨씬 시간복잡도도 공간복잡도도 절약할 수 있는 방법같다
# 강사 풀이를 보고 스스로 다시 작성한 코드 (전체 코드 시간복잡도 : O(N*M))
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
sum_list = [0] * (N + M + 1)

# O(N*M)
for i in range(1, N + 1):
  for j in range(1, M + 1):
    sum_list[i + j] += 1

# O(N*M)
maximum = max(sum_list)

# O(N*M)
for idx, value in enumerate(sum_list):
  if value == maximum:
    print(idx, end=" ")
