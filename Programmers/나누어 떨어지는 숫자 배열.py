def solution(arr, divisor):
    answer = [i for i in arr if i%divisor==0]
    
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)
