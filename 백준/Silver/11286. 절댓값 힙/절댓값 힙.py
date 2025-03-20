import sys, heapq

input = sys.stdin.readline

N = int(input())

min_heap = []
max_heap = []

for _ in range(N):
    num = int(input())
    if num > 0 :
        heapq.heappush(min_heap, num)
    elif num < 0 :
        heapq.heappush(max_heap, -num)
    else:
        if max_heap:
            if min_heap:
                if min_heap[0] < max_heap[0]:
                    print(heapq.heappop(min_heap))
                else:
                    print(-heapq.heappop(max_heap))
            else:
                print(-heapq.heappop(max_heap))
        elif min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)