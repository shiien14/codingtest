import sys

input = sys.stdin.readline

n = int(input())
requests=list(map(int, input().split()))
m = int(input())

requests.sort()

start, end = 0, requests[-1]
result = 0

while start <= end:
    mid = (start + end) // 2

    allocated = sum(min(r, mid) for r in requests)

    if allocated <= m :
        result = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(result)