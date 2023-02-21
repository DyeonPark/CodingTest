def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a%i==0 and b%i==0:
            return i

def lcm(a, b):
    for i in range(max(a, b), (a*b)+1):
        if i%a==0 and i%b==0:
            return i

def solution(numer1, denom1, numer2, denom2):
    
    answer = [0, 0]
    denom_lcm = lcm(denom1, denom2)
    
    # set denom for result fountain
    answer[1] = denom_lcm
    
    # first fountain    
    denom_lcm_1 = denom_lcm // denom1
    answer[0] = answer[0] + (numer1 * denom_lcm_1)
    
    # second fountain
    denom_lcm_2 = denom_lcm // denom2
    answer[0] = answer[0] + (numer2 * denom_lcm_2)
    
    # check 
    answer_gcd = gcd(answer[0], answer[1])
    answer[0] = answer[0] / answer_gcd
    answer[1] = answer[1] / answer_gcd
    
    return answer
