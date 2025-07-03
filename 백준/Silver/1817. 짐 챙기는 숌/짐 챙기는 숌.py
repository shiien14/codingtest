import sys

input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))

if n==0:
    print(0)
else:
    box=1
    w=0
    for i in range(n-1,-1,-1):
        w+=books[i]
        if w<m:
            continue
        elif w>m:
            box+=1
            w=books[i]
        elif w==m:
            box+=1
            w=0

    if w==0:
        box-=1

    print(box)