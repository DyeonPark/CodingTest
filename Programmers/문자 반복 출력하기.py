def solution(my_string, n):
    
    answer = ''
    
    for i in my_string:
        answer = answer + (i*n)
        
    return answer
