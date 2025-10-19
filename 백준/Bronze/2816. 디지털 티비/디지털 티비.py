import sys

input = sys.stdin.readline

n = int(input())
channels=[input().strip() for _ in range(n)]

id1, id2 = channels.index('KBS1'), channels.index('KBS2')

if id1>id2:
    id2+=1

print('1'*id1+'4'*id1+'1'*id2+'4'*(id2-1))