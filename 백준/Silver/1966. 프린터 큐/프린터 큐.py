from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))

    queue = deque((i, p) for i, p in enumerate(priorities)) 
    count = 0

    while queue:
        max_priority = max(queue, key=lambda x: x[1])[1] 
        idx, priority = queue.popleft()

        if priority == max_priority:
            count += 1
            if idx == m: 
                print(count)
                break
        else:
            queue.append((idx, priority)) 
