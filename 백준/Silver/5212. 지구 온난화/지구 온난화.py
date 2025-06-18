import sys

input = sys.stdin.readline

r,c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]


new_board = [row[:] for row in board]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    for j in range(c):
        if board[i][j] == 'X':
            sea = 0
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < r and 0 <= nj < c:
                    if board[ni][nj] == '.':
                        sea += 1
                else:
                    sea += 1 
            if sea >= 3:
                new_board[i][j] = '.'

# print(new_board)

min_r, max_r = r, 0
min_c, max_c = c, 0

for i in range(r):
    for j in range(c):
        if new_board[i][j] == 'X':
            min_r,max_r  = min(min_r, i), max(max_r, i)
            min_c,max_c  = min(min_c, j), max(max_c, j)

for i in range(min_r, max_r + 1):
    print("".join(new_board[i][min_c:max_c + 1]))