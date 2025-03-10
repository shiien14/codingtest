import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(shark_x, shark_y, shark_size, grid, N):
    queue = deque([(shark_x, shark_y, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[shark_x][shark_y] = True
    fish_list = []
    min_dist = float('inf')
    
    while queue:
        x, y, dist = queue.popleft()
        
        if 0 < grid[x][y] < shark_size:
            if dist < min_dist:
                fish_list = [(x, y, dist)]
                min_dist = dist
            elif dist == min_dist:
                fish_list.append((x, y, dist))
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if grid[nx][ny] <= shark_size:
                    queue.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
    
    if fish_list:
        fish_list.sort()
        return fish_list[0]
    return None

def solve(N, grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                shark_x, shark_y = i, j
                grid[i][j] = 0
    
    shark_size = 2
    eat_count = 0
    total_time = 0
    
    while True:
        result = bfs(shark_x, shark_y, shark_size, grid, N)
        if not result:
            break 
        
        fish_x, fish_y, dist = result
        grid[fish_x][fish_y] = 0 
        total_time += dist
        eat_count += 1
        
        if eat_count == shark_size:
            shark_size += 1
            eat_count = 0

        shark_x, shark_y = fish_x, fish_y
    
    return total_time

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

print(solve(N, grid))