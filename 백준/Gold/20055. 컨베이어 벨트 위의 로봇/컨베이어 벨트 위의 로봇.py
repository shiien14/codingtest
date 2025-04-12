import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0]*N)
cnt = 0

while True :
    cnt+=1
    belt.rotate(1)
    robot.rotate(1)

    robot[-1]=0

    for i in range(N-2,-1,-1):
        if belt[i+1]>=1 and robot[i+1]==0 and robot[i]==1:
            robot[i+1]=1
            robot[i]=0
            belt[i+1]-=1
    robot[-1]=0
    
    if belt[0]>0:
        robot[0]=1
        belt[0]-=1
    if belt.count(0)>=K:
        break

print(cnt)