import sys

input = sys.stdin.readline

N = int(input())

board = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for r in range(y, y + 10):
        for c in range(x, x + 10):
            board[r][c] = 1

answer = sum(sum(row) for row in board)
print(answer)