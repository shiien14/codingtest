import sys

input = sys.stdin.readline

N,M = map(int, input().split())
nums = list(map(int, input().split()))
sums=[0]

for i in nums:
    sums.append(sums[-1]+i)

for _ in range(M):
    i,j = map(int, input().split())
    print(sums[j]-sums[i-1])