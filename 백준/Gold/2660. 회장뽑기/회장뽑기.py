import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

members = [[] for _ in range(n + 1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    members[a].append(b)
    members[b].append(a)

scores = [0] * (n + 1)

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)

    queue = deque()
    queue.append(i)
    visited[i] = True

    while queue:
        current = queue.popleft()
        for neighbor in members[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)

    scores[i] = max(dist[1:])

min_score = min(scores[1:])
candidates = []

for i in range(1, n + 1):
    if scores[i] == min_score:
        candidates.append(i)

print(min_score, len(candidates))
print(' '.join(map(str, candidates)))