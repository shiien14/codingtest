import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    result = 0
    max_price = 0

    for i in range(n-1,-1,-1):
        if max_price < prices[i]:
            max_price = prices[i]
        else:
            result += max_price - prices[i]

    print(result)