def solution(array):
    
    dictionary = {}
    
    # counting
    for i in array:
        if i in dictionary.keys():
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    
    # finding max
    answer = 0
    max_value = max(dictionary.values())
    if list(dictionary.values()).count(max_value) >= 2:
        answer = -1
    else:
        answer = max(dictionary.keys(), key=(lambda k: dictionary[k]))
    
    return answer
