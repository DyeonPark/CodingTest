# solved : 8m
import sys
input = sys.stdin.readline

# 에라토스테네스의 체
MAX_SIZE = 100000
prime_list = [1] * (MAX_SIZE + 1)
prime_list[0] = 0
prime_list[1] = 0

for i in range(2, MAX_SIZE + 1):
    if prime_list[i] == 1: # 반복문을 도는 횟수를 줄이기 위해서 if문을 추가
        j = 2
        while j * i <= MAX_SIZE:
            prime_list[j * i] = 0
            j += 1

def isPrime(x): # 강의 풀이는 이 부분을 for문을 돌며 해당 숫자가 소수인지 판별하는 방식으로 풀이하였음
    return prime_list[x]

def reverse(x): # 강의 풀이는 이 부분을 '% 10', '* 10', '// 10' 연산을 사용하여 풀이하였음
    return int(str(x)[::-1])

N = int(input())
nums = list(map(int, input().split()))

for num in nums:
    reversed_num = reverse(num)
    if isPrime(reversed_num):
        print(reversed_num, end=' ')
