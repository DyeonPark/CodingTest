# 정확성 100% 통과, 효율성 0% 통과
def solution(phone_book):
    
    phone_book.sort()
    
    answer = True
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                answer = False
                break
    
    return answer

# 정확성 90%(20문제 중 2문제 틀림) 효율성 100%
def solution(phone_book):
    
    phone_book.sort()
    len_list = sorted(list(set([len(i) for i in phone_book])))
    
    answer = True
    for i in len_list:
        tmp = set([num[:i] for num in phone_book])
        if len(tmp) < len(phone_book):
            answer = False
    
    return answer

