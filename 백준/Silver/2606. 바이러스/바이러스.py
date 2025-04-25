import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

N=int(input())
L=int(input())
line=[[] for _ in range(N+1)]

for _ in range(L):
    a,b=map(int, input().split())
    line[a].append(b)
    line[b].append(a)

visited=[0]*(N+1)

def dfs(R):
    visited[R]=1  
    count = 1
    for i in line[R]:
        if not visited[i]:
            count += dfs(i)
            
    return count

print(dfs(1)-1)