import sys

input = sys.stdin.readline

T=int(input())

result0=[0]*41
result1=[0]*41

for i in range(41):
    if i == 0:
        result0[i] = 1
        result1[i] = 0
    elif i == 1: 
        result0[i] = 0
        result1[i] = 1
    else:
        result0[i] = result0[i-1] + result0[i-2]
        result1[i] = result1[i-1] + result1[i-2]


for _ in range(T):
    n = int(input())
    print(result0[n], result1[n])