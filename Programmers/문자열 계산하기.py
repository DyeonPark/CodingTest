import re

def solution(my_string):
    
    my_string = my_string.replace(' ', '')
    results = list(map(int,re.split('[+-]', my_string)))
    
    oper_list = [i for i in my_string if i in ('+', '-')]
    
    for idx, val in enumerate(oper_list):
        if val == '+':
            results[idx + 1] = results[idx] + results[idx + 1]
        elif val == '-':
            results[idx + 1] = results[idx] - results[idx + 1]
        else:
            continue
            
    return results[-1]
