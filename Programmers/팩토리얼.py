def solution(n):
    
    total, i = 1, 1
    
    while True:
        i += 1
        total *= i
        
        if total == n:
            return i
        elif total > n:
            return i-1
        else:
            continue
        
    return i
