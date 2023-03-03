def solution(t, p):
    
    len_str = len(p)
    tmp_list = []
    
    for i in range(0, len(t)-len_str+1):
        tmp_list.append(int(t[i:i+len_str]))
    
    answer = 0
    for i in tmp_list:
        if int(p) >= i:
            answer += 1
    
    return answer
