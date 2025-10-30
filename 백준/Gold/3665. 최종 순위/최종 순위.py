import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    rank = list(map(int, input().split()))
    graph=[[] for _ in range(n+1)]
    indegree=[0 for _ in range(n+1)]
    flag=0

    for i in range(n-1):
        for j in range(i+1,n):
            graph[rank[i]].append(rank[j])
            indegree[rank[j]]+=1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        flag=1

        for i in graph[a]:
            if i==b:
                graph[a].remove(b)
                indegree[b]-=1
                graph[b].append(a)
                indegree[a]+=1
                flag=0
        
        if flag:
            graph[b].remove(a)
            indegree[a]-=1
            graph[a].append(b)
            indegree[b]+=1


    q = deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    if not q:
        print("IMPOSSIBLE")
        continue

    answer=[]
    result=True
    while q:
        if len(q)>1:
            result = False
            break

        current = q.popleft()
        answer.append(current)
        for next in graph[current]:
            indegree[next]-=1
            if indegree[next]==0:
                q.append(next)
            elif indegree[next]<0:
                result=False
                break
    
    if not result or len(answer)<n:
        print("IMPOSSIBLE")
    else:
        print(*answer)