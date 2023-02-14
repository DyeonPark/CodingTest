def solution(my_string, num1, num2):
    
    list_string = list(my_string)
    
    tmp = list_string[num1]
    list_string[num1] = list_string[num2]
    list_string[num2] = tmp
    
    return ''.join(list_string)
