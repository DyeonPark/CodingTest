import math

def solution(n):
    answer = math.sqrt(n)
    if answer.is_integer():
        return (answer+1)**2
    else:
        return -1
