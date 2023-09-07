# solved : 7m
# 에라토스테네스의 체 : 소수가 아닌 것을 지워나가는 것 (소수를 구하는 방법 중 가장 빠르다고 함)
import sys
input = sys.stdin.readline

N = int(input())
nums = [1] * (N + 1)
nums[0] = 0  # 소수가 아닌 것은 0으로 지우기
nums[1] = 0

for i in range(2, N + 1):
    j = 2
    while j * i <= N: # 배수는 소수가 아니므로, 0으로 지우기
        nums[j * i] = 0
        j += 1

print(sum(nums))

# 강의 풀이 (시간복잡도: O(N))
# 강의 풀이의 특징 : if문을 적절히 사용하여 for문을 도는 횟수를 최대한 줄이는 것 같음
import sys
input = sys.stdin.readline

N = int(input())
prime_list = [0] * (N + 1)

cnt = 0
for i in range(2, N + 1):
  if prime_list[i] == 0: # 이미 본 것인지 아닌지 판단하는 if문 -> 이를 통해 첫 번째 풀이보다 for문을 도는 수를 줄일 수 있다
    cnt += 1
    for j in range(i, N + 1, i): # 배수는 소수가 아니므로, 1로 처리
      prime_list[j] = 1

print(cnt)
