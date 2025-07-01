import sys

input = sys.stdin.readline

n = int(input())

task = []
score = 0
for _ in range(n):
    info = list(map(int, input().split()))
    if info[0] == 1:
        task.append([info[1], info[2]-1])
    elif info[0] == 0 and task :
        task[-1][1] -=1
    elif not task and info[0] == 0:
        continue
    
    if task[-1][-1] == 0:
        score += task[-1][0]
        task.pop()
    
print(score)