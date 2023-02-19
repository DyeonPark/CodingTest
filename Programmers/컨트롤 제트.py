def solution(s):
    
    answer = []
    s = list(s.split())
    
    for i in s:
        if i == "Z" and len(answer) != 0:
            answer.pop()
        elif i == "Z" and len(answer) == 0:
            pass
        else:
            answer.append(int(i))
    
    return sum(answer)
