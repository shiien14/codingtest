import sys

N = int(sys.stdin.readline())
cost = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

answer=10000000
for i in range(3):
    dp=[[1000,1000,1000] for _ in range(N)]
    dp[0][i]=cost[0][i]

    for j in range(1,N):
        dp[j][0]= cost[j][0]+min(dp[j-1][1], dp[j-1][2])
        dp[j][1]= cost[j][1]+min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = cost[j][2]+min(dp[j-1][0], dp[j-1][1])

    for k in range(3):
        if i != k:
            answer=min(answer,dp[-1][k])

print(answer)