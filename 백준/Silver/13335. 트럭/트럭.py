import sys
from collections import deque
input = sys.stdin.readline

n,w,l = map(int, input().split())
trucks= deque(map(int, input().split()))

bridge = deque([0] * w)
time = 0 
weight = 0

while bridge:
    time += 1
    out = bridge.popleft()
    weight -= out

    if trucks:
        if weight + trucks[0] <= l:
            t = trucks.popleft()
            bridge.append(t)
            weight += t
        else:
            bridge.append(0)
print(time)