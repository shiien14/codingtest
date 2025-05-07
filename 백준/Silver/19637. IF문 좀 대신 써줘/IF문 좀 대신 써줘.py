import sys

input = sys.stdin.readline

n, m = map(int, input().split())
titles = []
for _ in range(n):
    name, limit = input().split()
    if titles and titles[-1][1] == int(limit):
        continue
    titles.append([name, int(limit)])

for _ in range(m):
    ch = int(input())

    start = 0
    end = len(titles)-1

    while start <= end:
        mid = (start+end)//2

        if titles[mid][1] < ch:
            start = mid+1
        else:
            end = mid-1

    print(titles[end+1][0])