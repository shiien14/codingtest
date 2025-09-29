import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

stand = Counter(words[0])
base = len(words[0])

cnt=0
for i in range(1, n):
    com = Counter(words[i])
    diff_len = abs(base - len(words[i]))

    if diff_len >= 2:
        continue

    total_diff = 0
    for k in set(stand.keys()) | set(com.keys()):
        total_diff += abs(stand[k] - com[k])

    if diff_len == 0:
        if total_diff <= 2:
            cnt += 1
    else:
        if total_diff <= 1:
            cnt += 1

print(cnt)