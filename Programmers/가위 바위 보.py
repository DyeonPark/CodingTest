def solution(rsp):
    answer = ''
    
    for i in rsp:
        if i == "0":
            answer += '5'
        elif i == "2":
            answer += '0'
        else:  # i == "5"
            answer += '2'
    
    return answer
