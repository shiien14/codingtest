import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y, x):
    global graph, visited, result
    visited[y][x] = True

    if y == (M - 1):
        result = "YES"

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx] and not graph[ny][nx]:
            dfs(ny, nx)

    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

M, N = map(int, input().split())
graph = []
visited = [[False] * N for _ in range(M)]
result = "NO"

for i in range(M):
    graph.append(list(map(int, input().rstrip())))

for i in range(N):
    if not visited[0][i] and not graph[0][i]:
        dfs(0, i)

print(result)