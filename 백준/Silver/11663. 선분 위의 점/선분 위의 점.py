import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()

for _ in range(M):
    start, end = map(int, input().split())

    left = 0
    right = N - 1
    lower = N
    while left <= right:
        mid = (left + right) // 2
        if dots[mid] >= start:
            lower = mid
            right = mid - 1
        else:
            left = mid + 1

    left = 0
    right = N - 1
    upper = N
    while left <= right:
        mid = (left + right) // 2
        if dots[mid] > end:
            upper = mid
            right = mid - 1
        else:
            left = mid + 1

    print(upper - lower)