import sys
from collections import defaultdict

input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_len = 0
left, right, count = 0, 0, defaultdict(int)

while right < n:
    if count[arr[right]] < k:
        count[arr[right]] += 1
        right += 1
    else:
        count[arr[left]] -= 1
        left += 1
    max_len = max(max_len, right - left)
print(max_len)