import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
nums = [i for i in range(1,n+1)]
for per in permutations(nums):
    print(' '.join(map(str, per)))