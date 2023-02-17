def solution(my_string):
    
    check_list = []
    for i in my_string:
        if i not in check_list:
            check_list.append(i)
    
    answer = ''.join(check_list)
    return answer
