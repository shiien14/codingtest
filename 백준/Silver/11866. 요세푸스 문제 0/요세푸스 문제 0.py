import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
q = deque(range(1,n+1))

cnt=0
result =[]

while q:
    target=q.popleft()
    cnt+=1
    if cnt==k:
        cnt = 0
        result.append(target)
        continue
    q.append(target)

    # q.rotate(-(k-1))
    # result.append(q.popleft())

print("<"+", ".join(map(str,result))+">")