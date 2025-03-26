import sys

input = sys.stdin.readline

N = int(input())

num = 0
cnt = 0

while True:
    num+=cnt
    if num>N:
        break
    cnt+=1

print(cnt-1)