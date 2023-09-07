# solved : 21m
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
