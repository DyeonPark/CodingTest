def solution(s):
    answer = ''
    
    # counting - O(N)
    finded = {}
    for i in s:
        if i not in finded.keys():
            finded[i] = 1
        else:
            finded[i] += 1
            
    # filtering - O(N)
    for i in s:
        if finded[i] == 1:
            answer += i
            
    return ''.join(sorted(answer))
