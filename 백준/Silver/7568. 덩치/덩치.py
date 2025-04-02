import sys

input = sys.stdin.readline

N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]
result = [1 for _ in range(N)]

for i in range(N):
    cnt = 0
    for j in range(N):
        if i==j:
            continue
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            cnt+=1

    result[i] += cnt

for i in result:
    print(i, end=" ")