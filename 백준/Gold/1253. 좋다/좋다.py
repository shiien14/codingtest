import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
result = 0
nums.sort()

for i in range(N):
    num=nums[i]
    start=0
    end=N-1

    while start<end:
        sum=nums[start]+nums[end]
        if num==sum:
            if start!=i and end!=i:
                result+=1
                break
            elif i==start:
                start+=1
            elif i==end:
                end-=1
        elif num>sum:
            start+=1
        elif num<sum:
            end-=1

print(result)