import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

result = 0
l, r = 0, n-1
while l < r:
    temp = arr[l] + arr[r]
    if temp == x:
        result += 1
        l += 1
    elif temp < x:
        l += 1
    else:
        r -= 1

print(result)