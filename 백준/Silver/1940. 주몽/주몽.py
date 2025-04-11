import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
nums = list(map(int, input().split()))

nums.sort()

i=0
j=N-1
count=0

while i<j:
    sum = nums[i]+nums[j]
    if sum<M:
        i+=1
    elif sum>M:
        j-=1
    else:
        count+=1
        i+=1
        j-=1

print(count)