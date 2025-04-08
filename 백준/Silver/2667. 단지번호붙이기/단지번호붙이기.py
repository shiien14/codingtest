import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]

d = [[0,1], [1,0],[-1,0],[0,-1]]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y]=1
    count=1

    while q:
        x,y = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if map[nx][ny]==1:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    count+=1
    
    return count

result=[]
for i in range(n):
    for j in range(n):
        if map[i][j]==1 and visited[i][j]==0:
            result.append(bfs(i,j))
    
print(len(result))

for r in sorted(result):
    print(r)