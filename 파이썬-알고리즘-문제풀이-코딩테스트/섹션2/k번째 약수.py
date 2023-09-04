import sys
N, K = map(int, input().split())

cnt = 0
for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
        if cnt == K:
            print(i)
            break
else: # using for-else
    print(-1)
    
# if cnt < K:
#     print(-1)
