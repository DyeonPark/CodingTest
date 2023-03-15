def solution(absolutes, signs):
    
    answer = 0
    
    for idx in range(len(absolutes)):
        if signs[idx] == True:
            answer += absolutes[idx]
        else:
            answer -= absolutes[idx]
            
    return answer

# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
