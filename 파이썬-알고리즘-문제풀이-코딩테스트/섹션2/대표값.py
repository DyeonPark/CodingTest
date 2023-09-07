# solved : 8m
# 전체 코드 시간복잡도 : O(N)
import sys
import math
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
mean = round(sum(scores) / N)

diff = []
for i in scores: # O(N)
    diff.append(abs(i - mean))

minimum = min(diff) # O(N)
res = []
for i in range(N): # O(N)
    if diff[i] == minimum:
        res.append(scores[i])

maximum = max(res) # O(N)
print(mean, scores.index(maximum) + 1) # O(N)

# 강사 풀이
# 차이점 : if문을 좀 더 복잡하게 쓰기는 했지만, 시간복잡도를 훨씬 절약할 수 있음
minimum = sys.maxsize
score, res = 0, 0

for idx, value in scores:
    diff = abs(mean - score)
    if diff < minimum: # 차이가 더 작은 경우 (차이 최솟값이 업데이트 됨)
        score = value
        minimum = diff
        res = idx + 1 # 번호는 인덱스값보다 1이 더 큰 상태이기 때문
    elif diff == minimum: # 차이가 동일한 경우
        if value > score: # 해당 조건 덕분에 같은 값이면 맨 앞의 인덱스를 가져올 수 있게 됨
            score = value
            res = idx + 1

print(mean, res)
    
