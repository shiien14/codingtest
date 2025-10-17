import sys

input = sys.stdin.readline

while True:
    info = sorted(list(map(int, input().split())))
    if sum(info)== 0:
        break
    elif info[2]>=info[1]+info[0]:
        print("Invalid")
    elif info[0]==info[1] and info[1]==info[2] and info[2]==info[0]:
        print("Equilateral")
    elif info[0]==info[1] or info[1]==info[2] or info[2]==info[0]:
        print("Isosceles")
    else:
        print("Scalene")