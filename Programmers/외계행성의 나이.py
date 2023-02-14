def solution(age):
    
    age = str(age)
    table = age.maketrans('0123456789', 'abcdefghij')
    trans_age = age.translate(table)
    
    return trans_age
