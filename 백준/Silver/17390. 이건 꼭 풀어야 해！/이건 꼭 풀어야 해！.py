import sys
from itertools import accumulate

input = sys.stdin.readline

N,Q = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

sums = list(accumulate(nums))
sums.insert(0,0)

for _ in range(Q):
    L,R = map(int, input().split())
    print(sums[R]-sums[L-1])