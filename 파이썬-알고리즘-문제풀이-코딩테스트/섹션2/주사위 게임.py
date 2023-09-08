# solved: 15m
import sys
def input():
    return sys.stdin.readline().rstrip()

def cal_award(comb):
    top_num = max(comb) # O(6)
    if top_num == 3:
        return 10000 + (comb.index(top_num) + 1) * 1000
    elif top_num == 2:
        return 1000 + (comb.index(top_num) + 1) * 100
    else:
        for i in range(5, -1, -1):
            if comb[i] == 1:
                return (comb[i] + 1) * 100

N = int(input())

maximum = -(sys.maxsize)
for _ in range(N):
    dice = list(map(int, input().split()))
    
    comb = [0] * 6
    for i in dice:
        comb[i - 1] += 1
    
    maximum = max(maximum, cal_award(comb))

print(maximum)
