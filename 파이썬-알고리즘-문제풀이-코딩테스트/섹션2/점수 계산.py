# solved : 5m
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
correct = list(map(int, input().split()))
score = [0] * N

for i in range(N):
    if correct[i]:
        if i == 0 or correct[i - 1] == 0:
            score[i] = 1
        else:
            score[i] = score[i - 1] + 1
    else:
        score[i] = 0
        
print(sum(score))
