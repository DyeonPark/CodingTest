def solution(chicken):
    answer = 0
    coupon = 0
    
    coupon = chicken  # 처음 주문하는 경우
    
    while True:
        
        if coupon >= 10: # 쿠폰으로 재주문
            tmp = coupon // 10  
            answer += tmp
            coupon %= 10
            coupon += tmp
        else:
            break
            
    return answer
