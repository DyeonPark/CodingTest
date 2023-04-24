def solution(x):
    x_sum = sum([int(i) for i in str(x)])
    if x % x_sum == 0:
        return True
    else:
        return False
