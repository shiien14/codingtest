import sys

input = sys.stdin.readline

n, m = map(int, input().split())

map1=[]
for _ in range(n):
    map1.append(list(map(int,input().split())))

map2=[]
for _ in range(n):
    map2.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        print(map1[i][j]+map2[i][j], end=' ')
    print()