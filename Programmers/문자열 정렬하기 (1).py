import re

def solution(my_string):
    
    return sorted([int(i) for i in re.sub('[^0-9]','',my_string)])
