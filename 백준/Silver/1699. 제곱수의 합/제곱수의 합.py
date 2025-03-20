import sys

input = sys.stdin.readline

N = int(input())
dp = [i for i in range(N + 1)]

for i in range(2, N + 1):
    for j in range(2, i // 2 + 1):
        if j * j > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1

print(dp[N])