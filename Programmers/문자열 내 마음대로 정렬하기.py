def solution(strings, n):
    
    sort_n_arr = [i[n] for i in strings]
    sort_n_arr.sort()
    
    answer = []
    for check_char in sort_n_arr:
        
        cnt = 0
        tmp_list = []
        
        for idx, _str in enumerate(strings):
            
            if _str is not None and check_char == _str[n]:
                tmp_list.append(_str)
                strings[idx] = None
                
        tmp_list.sort() 
        answer.extend(tmp_list)
    
    return answer
