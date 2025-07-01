dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

visited = [[False]*6 for _ in range(6)]

route = []
for _ in range(36):
    p = input()
    x = ord(p[0]) - ord('A')
    y = int(p[1]) - 1
    route.append((x, y))

sx, sy = route[0]
visited[sx][sy] = True
cx, cy = sx, sy

valid = True

for i in range(1, 36):
    nx, ny = route[i]

    can_move = False
    for d in range(8):
        if cx + dx[d] == nx and cy + dy[d] == ny:
            can_move = True
            break

    if visited[nx][ny] or not can_move:
        valid = False
        break

    visited[nx][ny] = True
    cx, cy = nx, ny

can_move = False
for d in range(8):
    if cx + dx[d] == sx and cy + dy[d] == sy:
        can_move = True
        break

if not can_move:
    valid = False

print("Valid" if valid else "Invalid")
