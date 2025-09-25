import sys
input = sys.stdin.readline

n, d = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

filter = []
for triple in nums:
    s, e, c = triple
    if e <= d and c < e - s:
        filter.append((s, e, c))

dp = [i for i in range(d + 1)]

for i in range(d + 1):
    if i > 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)

    for s, e, c in filter:
        if s == i:
            if dp[e] > dp[i] + c:
                dp[e] = dp[i] + c

print(dp[d])