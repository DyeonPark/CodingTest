import sys

def input():
    return sys.stdin.readline().rstrip()

cards = [i for i in range(21)]

for _ in range(10):
    a, b = map(int, input().split())
    cards[a:b + 1] = list(reversed(cards[a:b + 1]))

for i in cards[1:]:
    print(i, end=' ') 
