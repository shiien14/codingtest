from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int, input().split())
dp = [-1] * 100001
dp[N] = 0
q = deque([N])

while q:
    s = q.popleft()
    if s==K:
        print(dp[s])
        break

    if 0 <= s-1 <100001 and dp[s-1] == -1:
        dp[s-1] = dp[s]+1
        q.append(s-1)

    if 0 < s*2 < 100001 and dp[s*2] == -1:
        dp[s*2] = dp[s]
        q.appendleft(s*2)

    if 0 <= s+1 < 100001 and dp[s+1] == -1:
        dp[s+1] = dp[s] + 1
        q.append(s+1)