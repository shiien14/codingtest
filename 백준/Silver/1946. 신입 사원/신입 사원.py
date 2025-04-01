import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(n)]

    scores.sort()
    cut = scores[0][1]

    cnt=1
    for score in scores:
        if cut>score[1]:
            cnt+=1
            cut=score[1]

    print(cnt)