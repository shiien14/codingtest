import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]

mis = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if (i + j) % 2 == 0:
            expected = 'B' 
        else: expected = 'W'
        mis[i][j] = 0 if board[i][j] == expected else 1

ps = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row_sum = 0
    for j in range(1, M + 1):
        row_sum += mis[i - 1][j - 1]
        ps[i][j] = ps[i - 1][j] + row_sum

answer = K * K
for i in range(K, N + 1):
    for j in range(K, M + 1):
        s = ps[i][j] - ps[i - K][j] - ps[i][j - K] + ps[i - K][j - K]
        repaint = s if s <= (K * K - s) else (K * K - s)
        if repaint < answer:
            answer = repaint

print(answer)