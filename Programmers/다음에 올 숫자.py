def is_degree_diff(common):
    first_diff = common[1]-common[0]
    second_diff = common[2]-common[1]
    
    if first_diff == second_diff:
        return True
    else:
        return False

def solution(common):
    
    if is_degree_diff(common):  # 등차수열
        return common[-1] + (common[1]-common[0])
    else:  # 등비수열
        return common[-1] * (common[1]//common[0])
        
