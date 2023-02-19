def solution(M, N):
    answer = 0
    M_count = 1
    N_count = 1
    
    while M > 1:
        M -= 1
        M_count += 1
        
    while N > 1:
        N -= 1
        answer += 1
        
    answer = M_count + ( M_count * answer) - 1
    
    return answer
