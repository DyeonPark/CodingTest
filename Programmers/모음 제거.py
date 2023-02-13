def solution(my_string):
    replace_dic = {
        'a':'',
        'i':'',
        'o':'',
        'u':'',
        'e':''
    }
    trans_table = my_string.maketrans(replace_dic)
    return my_string.translate(trans_table)
