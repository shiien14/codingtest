import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

def bfs():
    cheese = [list(map(int, input().split())) for _ in range(n)]
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    time = 0
    cnt = 0

    while True:
        visited = [[0] * m for _ in range(n)]
        q = deque([(0, 0)])
        melt_cheese = deque()
        visited[0][0] = 1  

  
        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    if cheese[nx][ny] == 0:
                        q.append((nx, ny))  
                    elif cheese[nx][ny] == 1:
                        melt_cheese.append((nx, ny))  

        if not melt_cheese: 
            break

        time += 1
        cnt = len(melt_cheese)


        while melt_cheese:
            x, y = melt_cheese.popleft()
            cheese[x][y] = 0

    return time,cnt

time, cnt = bfs()
print(time)
print(cnt)