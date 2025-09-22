import sys

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
x = list(map(int, input().split()))
x.sort()

answer = 0
answer = max(answer, x[0])
answer = max(answer , N-x[-1])

for i in range(1, M):
    dis = x[i]-x[i-1]
    leng = (dis+1)//2
    answer = max(answer, leng)

print(answer)