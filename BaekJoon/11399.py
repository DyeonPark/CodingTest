N = int(input())
waitings = list(map(int, input().split()))

waitings.sort() # NlogN

result = 0
for i in range(1, N+1):# N
  result += sum(waitings[:i])

print(result)

# Time complexity is O(N + NlogN) -> O(NlogN)
