import sys

input = sys.stdin.readline

nums = list(input().strip())
count1=nums.count('1')//2
count0=nums.count('0')//2

for _ in range(count1):
    nums.pop(nums.index('1'))

nums = nums[::-1]
for _ in range(count0):
    nums.pop(nums.index('0'))

nums = nums[::-1]
print(''.join(nums))