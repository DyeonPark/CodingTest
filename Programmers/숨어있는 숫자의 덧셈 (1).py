import re

def solution(my_string):
    return sum(list(int(i) for i in re.sub('[^0-9]','',my_string)))
