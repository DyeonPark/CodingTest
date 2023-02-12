def solution(str1, str2):
    for i in range(0, len(str1)-len(str2)+1):
        if str1[i:i+len(str2)] == str2:
            print(str1[i:i+len(str2)+1])
            return 1
    return 2
