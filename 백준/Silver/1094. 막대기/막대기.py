import sys

input= sys.stdin.readline

n = int(input())
sticks=[64,32,16,8,4,2,1]

cnt=0

for i in range(len(sticks)):
    if n==0:
        break
    if sticks[i]<=n:
        n-=sticks[i]
        cnt+=1

print(cnt)