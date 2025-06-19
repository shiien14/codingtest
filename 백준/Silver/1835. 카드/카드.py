import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q=deque()

for i in range(n,0,-1):
    q.appendleft(i)
    for _ in range(i):
        q.appendleft(q.pop())

print(" ".join(map(str, q)))