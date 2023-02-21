def solution(num, total):
        
    start_num = total + int(num/2)
    while True:
        num_list = [start_num - n for n in range(num)]
        
        if sum(num_list) == total:
            return sorted(num_list)
        else:
            start_num -= 1
        
