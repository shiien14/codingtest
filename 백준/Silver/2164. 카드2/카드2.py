import sys
from collections import deque

input = sys.stdin.readline
n = int(input().strip())
q = deque([i for i in range(1, n+1)])

while(len(q)>1):
    q.popleft()
    m = q.popleft()
    q.append(m)

print(q[0])