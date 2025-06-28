import sys
from collections import deque

input = sys.stdin.readline
t=[deque(input().strip()) for _ in range(4)]

n = int(input())
for _ in range(n):
    num, dir = map(int,input().split())
    if num ==1 :
        if t[0][2] != t[1][6]:
            if t[1][2] != t[2][6]:
                if t[2][2] != t[3][6]:
                    t[3].rotate(-dir)
                t[2].rotate(dir)
            t[1].rotate(-dir)
        t[0].rotate(dir)
    elif num == 2:
        if t[0][2] != t[1][6]:
            t[0].rotate(-dir)
        if t[1][2] != t[2][6]:
            if t[2][2] != t[3][6]:
                t[3].rotate(dir)
            t[2].rotate(-dir)
        t[1].rotate(dir)
    elif num ==3 :
        if t[1][2] != t[2][6]:
            if t[0][2] != t[1][6]:
                t[0].rotate(dir)
            t[1].rotate(-dir)
        if t[2][2] != t[3][6]:
            t[3].rotate(-dir)
        t[2].rotate(dir)
    elif num==4:
        if t[2][2] != t[3][6]:
            if t[1][2] != t[2][6]:
                if t[0][2] != t[1][6]:
                    t[0].rotate(-dir)
                t[1].rotate(dir)
            t[2].rotate(-dir)
        t[3].rotate(dir)

result = 0
if t[0][0] == '1':
    result+=1
if t[1][0] =='1':
    result+=2
if t[2][0]=='1':
    result+=4
if t[3][0]=='1':
    result+=8

print(result)