import sys
input = sys.stdin.readline

N, X = map(int, input().split())
voices = list(map(int, input().split()))

while True:
    for i in range(N):
        if voices[i] >= X:
            X += 1
        else:
            print(i + 1)
            sys.exit()
