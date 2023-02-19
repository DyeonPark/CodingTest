def solution(dots):
    
    x_list = [i[0] for i in dots]
    y_list = [i[1] for i in dots]
    
    return (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))
