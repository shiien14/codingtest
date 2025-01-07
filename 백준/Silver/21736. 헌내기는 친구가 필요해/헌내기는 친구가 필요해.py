import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n, m = map(int, input().split())
graph = list(input() for _ in range(n))
visited = [[0]*m for _ in range(n)]
cnt=0

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(x,y):
    global cnt
    visited[x][y]=1
    if graph[x][y]=='P':
        cnt+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if graph[nx][ny]!='X':
                bfs(nx,ny)

for i in range(n):
    for j in range(m):
        if graph[i][j]=='I':
            bfs(i,j)

if cnt==0:
    print('TT')
else:
    print(cnt)