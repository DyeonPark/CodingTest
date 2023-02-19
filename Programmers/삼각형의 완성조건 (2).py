def solution(sides):
    answer = 0

    # 가장 긴 변이 sides 리스트 내에 있는 경우
    answer += max(sides) - (max(sides) - min(sides))
    
    # 가장 긴 변이 주어지지 않은 경우
    answer += sum(sides) - max(sides) - 1
    
    
    return answer
