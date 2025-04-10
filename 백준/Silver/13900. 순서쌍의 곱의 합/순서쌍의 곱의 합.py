import sys

input = sys.stdin.readline

N=int(input())
nums = list(map(int, input().split()))
sums = sum(nums)

result=0
for n in nums:
    sums-=n
    result+=n*sums
print(result)