def solution(numbers):
    
    replace_dic = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    
    for i in replace_dic.keys():
        if i in numbers:
            numbers = numbers.replace(i, replace_dic[i])

    return int(numbers)
