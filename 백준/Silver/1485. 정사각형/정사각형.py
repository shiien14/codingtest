import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(4)]  # 네 개의 점 입력
    distances = []

    for i in range(4):
        for j in range(i + 1, 4):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            distances.append(dx * dx + dy * dy)

    distances.sort()

    if distances[0] == 0:
        print(0)
    else:
        if distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5] and distances[4] == 2 * distances[0]:
            print(1)
        else:
            print(0)
