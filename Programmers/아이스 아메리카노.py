def solution(money):
    answer = []
    
    cnt = 0
    while (money >= 0):
        
        cnt += 1
        money -= 5500
    
    answer.extend([cnt-1, money+5500])
    
    return answer
