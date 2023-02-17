def solution(bin1, bin2):
    answer = [0 for i in range(11)]
    
    for i in range(-len(bin1), 0):
        answer[i] += int(bin1[i])
        
    for i in range(-len(bin2), 0):
        answer[i] += int(bin2[i])
        
    for i in range(-1, -12, -1):
        if answer[i] >= 2:
            answer[i-1] += 1
            answer[i] -= 2
            
    cnt, result = 0, ""
    for i in range(0, len(answer)):
        if answer[i] == 1:
            cnt += 1
            
        if answer[i] == 1 and cnt >= 1:
            result += str(answer[i])
        elif answer[i] == 0 and cnt >= 1:
            result += str(answer[i])
        elif answer[i] == 0 and cnt < 1:
            pass

    if result == "":
        return "0"
    else:
        return result
    
    # answer = bin(int(bin1, 28 + int(bin2,2))[2:]
    
    return answer
    
