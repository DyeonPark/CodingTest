def solution(score):
    
    eval_list = [sum(i)/2 for i in score]
    rank_list = [0 for i in range(len(score))]
    rank = 1
    
    while sum(eval_list) != -1 * len(eval_list):

        max_value = max(eval_list)
        
        count = 0
        while max_value in eval_list:
            idx = eval_list.index(max_value)  # 해당 랭크의 성적 위치 파악
            eval_list[idx] = - 1  # 랭크를 계산한 성적은 고려하지 않도록 처리
            rank_list[idx] = rank  # 랭크 저장
            count += 1
            
        rank += count
    
    return rank_list
