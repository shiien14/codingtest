import sys

input = sys.stdin.readline

W,H = map(int, input().split())
N=int(input())
stores = [list(map(int, input().split())) for _ in range(N)]
DG_dir, DG_dist = map(int, input().split())

def find(direction, distance):
    if direction == 1:
        return distance
    elif direction == 4:
        return W + distance
    elif direction == 2:
        return 2 * W + H - distance
    elif direction == 3:
        return 2 * (W + H) - distance

total =  2 * (W + H)

DG = find(DG_dir, DG_dist)

result = 0
for direction, distance in stores:
    store = find(direction, distance)
    dist = abs(DG - store)
    result += min(dist, total - dist)

print(result)