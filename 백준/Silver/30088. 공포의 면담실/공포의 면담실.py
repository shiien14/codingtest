import sys

input = sys.stdin.readline

N = int(input())

hap = []
for _ in range(N):
    times = list(map(int, input().split()))
    hap.append(sum(times)-times[0])

hap.sort()
result=[0]*N
result[0]=hap[0]

for i in range(1,N):
    result[i]=result[i-1]+hap[i]

print(sum(result))