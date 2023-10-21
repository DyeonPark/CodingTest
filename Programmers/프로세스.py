from collections import deque

def solution(priorities, location):

    queue = deque(priorities)
    print_cnt = 0
    
    while queue:
        if queue.index(max(queue)) > 0:
            queue.append(queue.popleft())
            if location == 0:
                location = len(queue) - 1
            else:
                location -= 1
        else:
            print_cnt += 1
            queue.popleft()
            if location  == 0:
                break
            else:
                location -= 1
    
    return print_cnt
