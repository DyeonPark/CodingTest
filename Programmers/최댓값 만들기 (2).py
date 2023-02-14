from itertools import combinations

def solution(numbers):
    
    max = numbers[0] * numbers[1]
    
    for i in combinations(numbers, 2):
        if max < i[0] * i[1]:
            max = i[0] * i[1]
        
    return max
    
    
