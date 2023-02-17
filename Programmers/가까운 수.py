def solution(array, n):
    
    diff_list = [abs(n - i) for i in array]
    
    min_diff = min(diff_list)
    
    if diff_list.count(min(diff_list)) >= 2:
        min_list = [array[idx] for idx in range(len(diff_list)) if diff_list[idx] == min(diff_list)]
        return min(min_list)
    else:
        return array[diff_list.index(min(diff_list))]
    
