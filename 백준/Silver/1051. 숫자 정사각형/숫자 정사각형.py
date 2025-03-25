import sys

input = sys.stdin.readline

N, M = map(int, input().split())
info = [input().strip() for _ in range(N)]

size=1

for i in range(N):
    for j in range(M):
        for d in range(min(N,M)):
            if i + d >= N or j + d >= M:
                break

            if (info[i][j] == info[i+d][j] and info[i][j] == info[i][j+d] and info[i][j] == info[i+d][j+d]):
                size = max(size, (d+1)**2)

print(size)