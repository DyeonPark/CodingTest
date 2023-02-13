def solution(my_string):
    answer = ''
    for i in my_string:
        if i.islower(): # small case
            answer += i.upper()
        else: # large case
            answer += i.lower()
    return answer
