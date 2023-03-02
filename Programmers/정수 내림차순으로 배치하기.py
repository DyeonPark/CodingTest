def solution(n):
    answer = str(n)
    return int("".join(sorted(answer, reverse=True)))
