import sys
from collections import deque

input = sys.stdin.readline

n=int(input())
ballons = deque(enumerate(map(int, input().split())))

result = []
while ballons:
    idx, paper = ballons.popleft()
    result.append(idx+1)

    if paper>0:
        ballons.rotate(-(paper-1))
    else:
        ballons.rotate(-paper)

print(' '.join(map(str, result)))