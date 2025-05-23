import sys
input = sys.stdin.readline

N=int(input())
time=list(map(int, input().split()))

time.sort()
total=time[0]

for i in range(1,N):
    total += sum(time[:i+1])

print(total)