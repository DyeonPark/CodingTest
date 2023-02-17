def solution(i, j, k):
    answer = 0
    
    for value in range(i, j+1):
        answer += str(value).count(str(k))
    
    return answer
