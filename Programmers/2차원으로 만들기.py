def solution(num_list, n):
    answer = [num_list[i*n:i*n+n] for i in range(int(len(num_list)/n))]
    return answer
