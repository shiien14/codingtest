import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = [int(input().strip()) for _ in range(N)]

count = [0] * (d + 1)
distinct = 0

for i in range(k):
    x = belt[i]
    if count[x] == 0:
        distinct += 1
    count[x] += 1

ans = distinct + (1 if count[c] == 0 else 0)

for i in range(1, N):
    out = belt[(i - 1) % N]
    count[out] -= 1
    if count[out] == 0:
        distinct -= 1

    in_ = belt[(i + k - 1) % N]
    if count[in_] == 0:
        distinct += 1
    count[in_] += 1

    cur = distinct + (1 if count[c] == 0 else 0)
    if cur > ans:
        ans = cur

print(ans)