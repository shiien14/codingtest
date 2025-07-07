import sys

input = sys.stdin.readline

p, m = map(int, input().split())

rooms = []
for i in range(p):
    level, name = input().split()
    level = int(level)

    placed = False
    for room in rooms:
        if len(room) < m and abs(room[0][0] - level) <= 10:
            room.append([level, name])
            placed = True
            break

    if not placed:
        rooms.append([[level, name]])

for room in rooms:
    room.sort(key=lambda x: x[1])
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
        
    for player in room:
        print(player[0], player[1])