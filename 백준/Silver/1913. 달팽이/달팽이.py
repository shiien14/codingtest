import sys

input = sys.stdin.readline

N = int(input())
find_num = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [[0] * N for _ in range(N)]

x, y = N // 2, N // 2
board[x][y] = 1

find_x, find_y = x, y

num = 2 
length = 1
while num <= N * N:
    for d in range(4):
        for _ in range(length):
            x += dx[d]
            y += dy[d]
            if x < 0 or y < 0 or x >= N or y >= N:
                continue
            board[x][y] = num
            if num == find_num:
                find_x, find_y = x, y
            num += 1
        if d == 1 or d == 3:
            length += 1

for row in board:
    print(' '.join(map(str, row)))

print(find_x + 1, find_y + 1)