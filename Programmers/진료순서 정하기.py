def solution(emergency):
    
    answer = emergency.copy()
    
    for i in range(1, len(emergency)+1):
        max_idx = emergency.index(max(emergency))
        answer[max_idx] = i
        emergency[max_idx] = -1
    
    return answer
