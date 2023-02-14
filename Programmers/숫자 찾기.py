def solution(num, k):
    
    return -1 if str(num).find(str(k)) == -1 else str(num).find(str(k)) + 1
