def solution(n):
    i = 2
    i_list = []
    
    while i <= n:
        if n % i == 0:
            i_list.append(i)
            n /= i
        else:
            i += 1
    
    result = list(set(i_list))
    
    return sorted(result)
