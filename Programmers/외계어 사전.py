def solution(spell, dic):
    answer = 0
    
    for word in dic:
        
        inner_count = 0
        for char in spell:
            if word.count(char) >= 1:
                inner_count += 1
                
        if inner_count == len(spell):
            answer += 1

    if answer >= 1:
        return 1
    else:
        return 2
 
