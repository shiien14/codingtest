import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
result=0

while start<=end:
    mid = (start+end)//2

    get = sum(t - mid for t in trees if t > mid)

    if get>=m:
        result = mid
        start = mid+1
    else:
        end=mid-1

print(result)