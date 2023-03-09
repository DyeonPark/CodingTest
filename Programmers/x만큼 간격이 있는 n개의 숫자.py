def solution(x, n):

    answer = []
    for i in range(n):
        if len(answer) == 0:
            answer.append(x)
        else:
            answer.append(answer[-1] + x)
    
    return answer
