from collections import Counter

def solution(participant, completion):
    
    p_cnt = Counter(participant)
    c_cnt = Counter(completion)
    
    for i in list(set(participant)):
        if p_cnt[i] - c_cnt[i]:
            return i
