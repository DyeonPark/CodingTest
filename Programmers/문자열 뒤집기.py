def solution(my_string):
    
    tmp = []; answer = "";
    for i in my_string:
        tmp.insert(0, i)
    answer = "".join(tmp)
    
    return answer
