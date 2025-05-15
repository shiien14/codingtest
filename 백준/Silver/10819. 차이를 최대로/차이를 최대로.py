from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
max_value = 0

for p in permutations(a):
    temp = 0
    for i in range(n - 1):
        temp += abs(p[i] - p[i + 1])
    max_value = max(max_value, temp)

print(max_value)