def solution(quiz):
    
    answer = list(map(lambda x: "O" if eval(x[:x.find('=')-1]) == int(x[x.find('=')+1:]) else "X", quiz))
    
    return answer
