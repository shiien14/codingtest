import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())

location = [list(map(int, input().split())) for _ in range(n)]
combi = combinations(range(n), k)

result = 1000000

for com in combi:
    max_min_d=0
    for i in range(n):
        min_d = 1000000
        for j in com:
            distance = abs(location[i][0] - location[j][0]) + abs(location[i][1] - location[j][1])
            min_d = min(min_d, distance)
        max_min_d = max(max_min_d, min_d)
    result = min(result, max_min_d)
    
print(result)