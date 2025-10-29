import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())

answer = []
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n+1)]
queue = []


for i in range(m):
    first, second = map(int, input().split())
    graph[first].append(second)
    indegree[second] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    tmp = heapq.heappop(queue)
    answer.append(tmp)
    for i in graph[tmp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(queue, i)


print(" ".join(map(str, answer)))