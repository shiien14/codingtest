import sys
from collections import deque

input= sys.stdin.readline

n,m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

result = []
for _ in range(m):
    start, target = map(int, input().split())

    visited = [False] * (n + 1)

    q = deque()
    q.append((start, 0))
    visited[start] = True  

    answer = 0

    while q:
        cur, dist_sum = q.popleft()

        if cur == target:
            answer = dist_sum
            break

        for nxt, w in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, dist_sum + w))

    result.append(str(answer))

print("\n".join(result))