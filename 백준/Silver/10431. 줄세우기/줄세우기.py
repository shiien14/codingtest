import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    test=list(map(int, input().split()))
    num = test[0]
    students = test[2:]
    cnt=0
    line = [test[1]]
    for s in students:
        if s > line[-1]:
            line.append(s)
        else:
            for i in range(len(line)):
                if s < line[i]:
                    cnt+=len(line)-i
                    line.insert(i,s)
                    break

    print(num, cnt)