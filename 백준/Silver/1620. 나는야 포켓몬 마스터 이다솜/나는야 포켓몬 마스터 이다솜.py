import sys

input = sys.stdin.readline

N,M = map(int, input().split())

pocketmon = {}

for i in range(N):
    name = input().strip()
    pocketmon[i+1] = name
    pocketmon[name] = i+1

for _ in range(M):
    find = input().strip()
    if find.isdigit():
        print(pocketmon[int(find)])
    else:
        print(pocketmon[find])