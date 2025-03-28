import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q=deque()

for _ in range(N):
    info = input().split()
    
    if info[0] == 'push':
        q.append(int(info[1]))
    elif info[0] == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif info[0] == 'size':
        print(len(q))
    elif info[0] == 'empty':
        if len(q) == 0 :
            print(1)
        else:
            print(0)
    elif info[0] == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif info[0] == 'back':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)