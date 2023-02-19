# from itertools import combinations

# def solution(balls, share):
    
#     numerator = 1
#     # numerator - 분자
#     for i in range(balls, share-1, -1):
#         numerator *= i
    
#     # denominator - 분모
#     denominator = 1
#     for i in range(share, 0 , -1):
#         denominator *= i
    
#     print(numerator, denominator)
        
#     return numerator // denominator
    
#     # return long(len(list(combinations(list(range(balls)), share))))

def solution(balls, share):

    a=1
    b=1
    c=0
    for i in range(balls, 0 , -1) :
        a = a * i
        c +=1
        if c == share :
            break
    for i in range(share, 0, -1) :
        b = b * i

    answer = a//b
    return answer
