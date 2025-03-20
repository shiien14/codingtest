import sys, heapq

input = sys.stdin.readline

N = int(input())

nums = []

for _ in range(N):
    num = int(input())
    if num:
        heapq.heappush(nums,(abs(num), num))
    else:
        if nums:
            print(heapq.heappop(nums)[1])
        else:
            print(0)
