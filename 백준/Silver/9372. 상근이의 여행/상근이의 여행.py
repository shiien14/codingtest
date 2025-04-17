import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    flights = [list(map(int, input().split())) for _ in range(M)]
    print(N-1)