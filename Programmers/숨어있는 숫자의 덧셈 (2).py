import re

def solution(my_string):
    
    my_string = re.sub('[a-zA-Z]', ' ', my_string)
    int_list = list(map(int, my_string.split()))
    
    return sum(int_list)
