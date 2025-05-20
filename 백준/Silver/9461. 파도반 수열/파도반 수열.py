T = int(input())
dp = [1, 1, 1, 2, 2]

for i in range(4, 100):
    dp.append(dp[i] + dp[i - 4])

for _ in range(T):
    n = int(input())
    print(dp[n - 1])