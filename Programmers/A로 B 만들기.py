def solution(before, after):
    
    before_dict = {}
    for i in before:
        if i in before_dict.keys():
            before_dict[i] += 1
        else:
            before_dict[i] = 1
            
    for i in after:
        if i in before_dict.keys():
            before_dict[i] -= 1
        else:
            return 0
    
    for i in before_dict.values():
        if i is not 0:
            return 0
        
    return 1
