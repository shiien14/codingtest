import sys

input = sys.stdin.readline

king, stone, n = input().split()
n = int(n)
space = ['A','B','C','D','E','F','G','H']
king_x = space.index(king[0])
king_y = int(king[1])-1
stone_x = space.index(stone[0])
stone_y = int(stone[1])-1

moves = {
    'R': (1, 0),
    'L': (-1, 0),
    'B': (0, -1),
    'T': (0, 1),
    'RT': (1, 1),
    'LT': (-1, 1),
    'RB': (1, -1),
    'LB': (-1, -1),
}

for i in range(n):
    comment = input().strip()
    if comment in moves:
        dx, dy = moves[comment]
        nx, ny = king_x + dx, king_y + dy

    if 0 <= nx < 8 and 0 <= ny < 8:
        if nx == stone_x and ny == stone_y:
            nsx, nsy = stone_x + dx, stone_y + dy
            if 0 <= nsx < 8 and 0 <= nsy < 8:
                king_x, king_y = nx, ny
                stone_x, stone_y = nsx, nsy
        else:
            king_x, king_y = nx, ny

king = space[king_x]+str(king_y+1)
stone = space[stone_x]+str(stone_y+1)
print(king)
print(stone)