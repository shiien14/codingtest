import sys

input = sys.stdin.readline

N,Q = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

sums = [0]
for i in range(N):  
    sums.append(nums[i] + sums[i])  

for _ in range(Q):
    L,R = map(int, input().split())
    print(sums[R]-sums[L-1])