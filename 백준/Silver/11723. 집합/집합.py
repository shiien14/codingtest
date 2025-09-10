import sys

input = sys.stdin.readline

M = int(input())

S = []

for _ in range(M):
    command=input().strip()
    if command == 'all':
        S=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    elif command =='empty':
        S=[]
    else:
        command, num = command.split()
        num=int(num)
        if command == 'add':
            if num not in S:
                S.append(num)
        elif command =='remove':
            if num in S:
                S.remove(num)
        elif command =='check':
            if num in S:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.append(num)