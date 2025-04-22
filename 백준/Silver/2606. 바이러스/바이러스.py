import sys
from collections import deque
input=sys.stdin.readline

N=int(input()) # 컴퓨터 수
L=int(input()) # 연결 라인 수
line=[[] for _ in range(N+1) ]

for _ in range(L):
    a,b=map(int, input().split())
    line[a].append(b)
    line[b].append(a)

#print(line)

cnt=0
visited=[0]*(N+1) #방문확인
visited[0]=1
visited[1]=1

def dfs(R, cnt):
    visited[R]=1  
    tmp = 1
    for i in line[R]:
        if not visited[i]:
            tmp += dfs(i, cnt + tmp)
            
    return tmp

print(dfs(1, 0)-1)