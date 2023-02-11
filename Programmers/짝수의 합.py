def solution(n):
    
    total = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            total += i
            
    answer = total
    
    return answer
