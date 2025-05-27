import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
enter = deque()
for _ in range(n):
    enter.append(input().strip())

out = []
for _ in range(n):
    out.append(input().strip())

idx = 0
passed = set()
cnt = 0

for car in out:
    while enter and enter[0] in passed:
        enter.popleft()
    if car == enter[0]:
        enter.popleft()
    else:
        cnt += 1
        passed.add(car)

print(cnt)