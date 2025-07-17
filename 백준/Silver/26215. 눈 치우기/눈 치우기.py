import sys
import heapq

input = sys.stdin.readline

n = int(input())
snow = list(map(int, input().split()))

snow = [-s for s in snow]
heapq.heapify(snow)

time = 0
while len(snow) >= 2:
    a = -heapq.heappop(snow)
    b = -heapq.heappop(snow)

    a -= 1
    b -= 1
    time += 1

    if a > 0:
        heapq.heappush(snow, -a)
    if b > 0:
        heapq.heappush(snow, -b)

    if time > 1440:
        print(-1)
        exit()

if snow:
    last = -snow[0]
    time += last
    if time > 1440:
        print(-1)
    else:
        print(time)
else:
    print(time)