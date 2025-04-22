import sys

input= sys.stdin.readline


N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

def divide(x, y, size):
    color = matrix[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != color:
                half = size // 2
                return "(" + divide(x, y, half) + divide(x, y + half, half) + \
                    divide(x + half, y, half) + divide(x + half, y + half, half) + ")"
    return color

print(divide(0, 0, N))