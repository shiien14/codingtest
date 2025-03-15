import sys
from math import comb

input = sys.stdin.readline

N = int(input())
M = int(input())

print(comb(M-1,N-1))