import sys
from collections import deque

input= sys.stdin.readline

n,m = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

visited=[[-1]*m for _ in range(n)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 0

    while q:
        i, j = q.popleft()

        for k in range(4):
            nx, ny = dx[k]+i, dy[k]+j
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
                if maps[nx][ny]==1:
                    visited[nx][ny]=visited[i][j]+1
                    q.append((nx,ny))

x_start,y_start=0,0
for i in range(n):
    for j in range(m):
        if maps[i][j]==2:
            x_start,y_start=i,j
        elif maps[i][j]==0:
            visited[i][j]=0

bfs(x_start,y_start)

for i in range(n):
    for j in range(m):
        print(visited[i][j], end=' ')
    print()