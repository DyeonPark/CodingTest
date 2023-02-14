def solution(order):
    answer = 0
    
    check = ['3', '6', '9']
    for i in str(order):
        if i in check:
            answer += 1
    
    return answer
