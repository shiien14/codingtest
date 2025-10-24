import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    result=[]
    num = int(input())
    result.append(num//25)
    num%=25
    result.append(num//10)
    num%=10
    result.append(num//5)
    num%=5
    result.append(num)
    print(*result)