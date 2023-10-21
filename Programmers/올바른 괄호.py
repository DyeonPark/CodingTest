def solution(s):
    stack = []
    
    is_closed = True
    for i in s:
        if i == "(":
            stack.append(i)
        else: # ")"
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                is_closed = False
                break
            
    if not stack and is_closed:
        return True
    else:
        return False
