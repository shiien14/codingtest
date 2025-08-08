from collections import deque

def solution(maps):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    
    n = len(maps)
    m = len(maps[0])
    
    visited= [[0] * m for _ in range(n)]
    q=deque()
    q.append((0,0,1))
    
    while q:
        x,y,cnt=q.popleft()
        if x == n-1 and y == m-1:
            return cnt
    
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny,cnt+1))      

    return -1