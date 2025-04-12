import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
q=deque()
nums = list(map(int, input().split()))

for i in range(N):
    while q and q[-1][0] > nums[i]:
        q.pop()
    q.append((nums[i],i))
    if q[0][1]<= i-L:
        q.popleft()
    print(q[0][0],end=' ')