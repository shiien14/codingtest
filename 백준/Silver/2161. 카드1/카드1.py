import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
nums = deque([])

for i in range(n) : 
    nums.append(i+1)

while len(nums) >1:
    print(nums.popleft(), end = ' ')
    nums.append(nums[0])
    nums.popleft()
print(nums[0], end = '')