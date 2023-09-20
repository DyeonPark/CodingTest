import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

# 내장 함수를 사용한 경우 (case 1)
n_list.extend(m_list)
n_list.sort()

for i in n_list:
    print(i, end=" ")

# 병합정렬의 원리를 사용한 경우 (case 2)
i = 0
j = 0
result = []
while True:
    if n_list[i] < m_list[j]:
        result.append(n_list[i])
        i += 1
    elif n_list[i] == m_list[j]:
        result.extend([n_list[i], m_list[j]])
        i += 1
        j += 1
    else: # i > j
        result.append(m_list[j])
        j += 1
    
    if i >= N or j >= M:
        break
    
if i < N:
    result.extend(n_list[i:])
elif j < M:
    result.extend(m_list[j:])
    
for i in result:
    print(i, end=" ")
