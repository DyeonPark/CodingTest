# solved : 8m
import sys
input = sys.stdin.readline

# 에라토스테네스의 체
MAX_SIZE = 100000
prime_list = [1] * (MAX_SIZE + 1)
prime_list[0] = 0
prime_list[1] = 0

for i in range(2, MAX_SIZE):
    j = 2
    while j * i <= MAX_SIZE:
        prime_list[j * i] = 0
        j += 1

def isPrime(x):
    return prime_list[x]

def reverse(x):
    return int(str(x)[::-1])

N = int(input())
nums = list(map(int, input().split()))

for num in nums:
    reversed_num = reverse(num)
    if isPrime(reversed_num):
        print(reversed_num, end=' ')
