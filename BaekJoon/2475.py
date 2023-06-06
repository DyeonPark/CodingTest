nums = list(map(int, input().split()))
nums_doubled = list(map(lambda x: x ** 2, nums))
print(sum(nums_doubled) % 10)
