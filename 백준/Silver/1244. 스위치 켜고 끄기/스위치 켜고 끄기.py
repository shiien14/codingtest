import sys

input = sys.stdin.readline

n = int(input())  

switch = list(map(int, input().split()))  

s = int(input())


for _ in range(s):
    gender, num = map(int, input().split())
    
    if gender == 1:
        
        for i in range(num - 1, n, num):
            switch[i] = 1 - switch[i]

    else: 
        i = num - 1 
        left = right = i

        while left > 0 and right < n - 1 and switch[left - 1] == switch[right + 1]:
            left -= 1
            right += 1

        for j in range(left, right + 1):
            switch[j] = 1 - switch[j]

for i in range(n):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:
        print()