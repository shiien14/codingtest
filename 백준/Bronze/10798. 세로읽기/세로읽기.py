import sys

input = sys.stdin.readline

letters = [input().strip() for _ in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(letters[i]):
            print(letters[i][j], end='')