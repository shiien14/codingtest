import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values=[]
for _ in range(n):
    values.append(int(input()))
    
dp = [0]*(k+1)
dp[0]=1

for v in values:
    for i in range(v, k+1):
        dp[i]+=dp[i-v]
print(dp[k])
    