def move(order):
    if order == "left":
        return [-1, 0]
    elif order == "right":
        return [1, 0]
    elif order == "up":
        return [0, 1]
    else:
        return [0, -1]
    
def solution(keyinput, board):
    answer = [0, 0]
    
    for order in keyinput:
        expect = move(order)
        
        # check x size
        if abs(answer[0] + expect[0]) <= abs(board[0] // 2):
            answer[0] = answer[0] + expect[0]
        else:
            pass
        
        # check y size
        if abs(answer[1] + expect[1]) <= abs(board[1] // 2):
            answer[1] = answer[1] + expect[1]
        else:
            pass
        
    
    return answer
