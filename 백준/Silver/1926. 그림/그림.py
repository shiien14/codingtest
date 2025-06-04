import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global size

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            size += 1
            dfs(nx, ny)



n, m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

M = 0
cnt = 0
for i in range(m):
    for j in range(n):
        if graph[j][i] == 1:
            size = 1
            graph[j][i] = -1
            dfs(i, j)
            cnt += 1
            temp = size
            if temp > M:
                M = temp

print(cnt)
print(M)