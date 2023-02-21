def solution(numlist, n):
    numlist.sort(reverse = True)
    abs_list = [abs(i-n) for i in numlist]
    
    answer = []
    while len(answer) != len(numlist):
        min_idx = abs_list.index(min(abs_list))
        answer.append(numlist[min_idx])
        abs_list[min_idx] = 10001
    
    return answer
