import sys

input = sys.stdin.readline

R,C,K = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

visited = [[False]*C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start_x, start_y = R - 1, 0
end_x, end_y = 0, C - 1

result = 0

def dfs(x, y, count):
    global result

    if x == end_x and y == end_y:
        if count == K:
            result += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and graph[nx][ny] != 'T':
                visited[nx][ny] = True
                dfs(nx, ny, count + 1)
                visited[nx][ny] = False

visited[start_x][start_y] = True
dfs(start_x, start_y, 1)

print(result)