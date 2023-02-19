def solution(my_str, n):
    
    return [my_str[i : i + n]for i in range(0, len(my_str), n)]

#     answer =  [my_str[i*n:(i*n)+n]for i in range(0, len(my_str)//n)]
#     if len(my_str) % n == 0:
#         pass
#     else:
#         answer.append(my_str[-(len(my_str) % n):])
    
#     return answer
