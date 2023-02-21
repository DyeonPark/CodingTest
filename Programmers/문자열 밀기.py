import math

def solution(A, B):
    if A == B:
        return 0
    else:
        for i in range(len(A)-1, 0, -1):
            test_str = A[i:] + A[:i]
            if test_str == B:
                return len(A) - i
        return -1
