import sys

input = sys.stdin.readline

n = int(input())

arr=[]

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        arr.append(command[1])
    elif command[0] == 'pop':
        if arr:
            print(arr.pop())
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(arr))
    elif command[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    else:
        if arr:
            print(arr[-1])
        else:
            print('-1')
