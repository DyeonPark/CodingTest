def find_gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i ==0 and b % i == 0:
            return i
    
def solution(a, b):
    
    after_b = int(b / find_gcd(a, b))
    print(after_b)
    
    i = 2
    while i <= after_b:
        if after_b % i == 0:
            if (i != 2) and (i != 5):
                return 2
            else:
                after_b /= i
        else:
            i += 1
            
    return 1
        
