def solution(new_id):
    # 1Step : 소문자로 변경
    answer = new_id.lower()

    # 2Step: 소문자, 숫자, 빼기, 밑줄, 마침표 제외 모두 제거
    deleteList = []
    for i in range(0, len(answer)):
        if (answer[i] == '-' or  # 빼기
                answer[i] == '_' or  # 밑줄
                answer[i] == '.' or  # 마침표
                (ord(answer[i]) >= 48 and ord(answer[i]) <= 57) or  # 숫자
                (ord(answer[i]) >= 97 and ord(answer[i]) <= 122)):  # 소문자
            continue
        else:
            deleteList.append(answer[i])

    for i in deleteList:
        answer = answer.replace(i, "")

    # 3Step: 연속된 마침표를 하나의 마침표로 치환
    if (answer.count("..") >= 1):
        for i in range(0, answer.count(".")):
            answer = answer.replace("..", ".")

    # 4Step: 아이디의 처음에 위치한 마침표 제거
    if (answer[0] == '.'):
        answer = answer[1:]

    # 5Step: 빈 문자열이라면 'a'대입
    if (len(answer) == 0):
        answer += 'a'

    # 6Step: 16자 이상이면 15자로 자르고, 맨 뒤가 마침표이면 마침표 제거
    if (len(answer) >= 16):
        answer = answer[:15]

    if (answer[len(answer) - 1] == '.'):
        answer = answer[:-1]

    # 7Step: new_id 길이가 2자 이하일 시, 마지막 문자를 길이 3이상 될때까지 붙임
    if (len(answer) <= 2):
        last_char = answer[-1]
        while (len(answer) < 3):
            answer = answer + last_char

    return answer
