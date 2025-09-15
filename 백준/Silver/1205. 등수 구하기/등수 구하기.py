import sys

input = sys.stdin.readline

n, new, p = map(int,input().split())
scores = list(map(int,input().split()))

if n == p and scores[-1] >= new:
        print(-1)
else:
    result = n + 1
    for i in range(n):
        if scores[i] <= new:
            result = i + 1
            break
    print(result)