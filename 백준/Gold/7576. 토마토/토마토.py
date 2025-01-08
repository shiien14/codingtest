from collections import deque
import sys
m,n = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] ==1:
            queue.append([i,j])

def bfs() :
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x +dx[i],y+dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<m:
                if graph[nx][ny]==0:
                    graph[nx][ny] =graph[x][y]+1
                    queue.append([nx,ny])

bfs()
maxresult = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            sys.exit()
        maxresult = max(maxresult,graph[i][j])

if maxresult ==1:
    print(0)
else :
    print(maxresult -1)