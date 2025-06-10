import sys

input = sys.stdin.readline

n = int(input())

for i in range(1,n+1):
    score = list(map(int,input().split()))
    M = max(score[1:])
    m = min(score[1:])
    score= sorted(score[1:], reverse=True)
    M_gap=0
    for j in range(len(score)):
        gap = score[j-1]-score[j]
        if gap>M_gap:
            M_gap = gap

    print("Class", i)
    print("Max", M, end=", ")
    print("Min", m, end =", ")
    print("Largest gap", M_gap)