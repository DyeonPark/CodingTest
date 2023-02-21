def solution(polynomial):
    
    if ' + ' in polynomial:  # 다항

        poly_list = polynomial.split(' + ')
        x_list = [1 if len(i) == 1 else int(i[:-1]) for i in poly_list if 'x' in i]
        num_list = [int(i) for i in poly_list if 'x' not in i]
        
        answer = ''
        if len(x_list) > 0:
            if sum(x_list) == 1:  # 'x'항의 계수가 1인 경우
                answer = 'x'
            else:  # 'x'항의 계수가 1보다 큰 경우
                answer = str(sum(x_list)) + 'x'
        
        if sum(num_list) > 0:
            if len(answer) > 0:  # 'x'항이 있는 경우
                answer += " + " + str(sum(num_list))
            else:  # 'x'항이 없는 경우
                answer = str(sum(num_list))
            
        if len(answer) > 0:
            return answer
        else:
            return "0"
            
    else:  # 단일항
        return polynomial
    
