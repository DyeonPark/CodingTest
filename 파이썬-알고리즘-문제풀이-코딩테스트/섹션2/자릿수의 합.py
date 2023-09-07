# sovled : 3m
# 전체 코드 시간복잡도 : O(N*M)
# N : 숫자의 수
# M : 각 숫자의 자릿수(길이)

import sys
input = sys.stdin.readline

def digit_sum(x): # O(M)
    total = 0
    for i in str(x): # 강사풀이에서는 본 파트를 '% 10'과 '// 10'을 활용하여 풀이하는 경우도 소개하였음
        total += int(i)
    return total

N = int(input())
nums = list(map(int, input().split()))

res = []
for num in nums: # O(N)
    res.append(digit_sum(num)) # O(M) 
    # 강사 풀이에서는 본 구역에 대소비교를 통해 바로 최대값을 찾도록 하였음 -> 내 코드에 비해 시간복잡도 줄일 수 있음

print(nums[res.index(max(res))]) # O(N) + O(N)
