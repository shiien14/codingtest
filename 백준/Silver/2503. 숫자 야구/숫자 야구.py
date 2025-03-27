import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
Q = [list(map(int, input().split())) for _ in range(N)]

numbers = list(permutations([1,2,3,4,5,6,7,8,9],3))

result = 0

for num in numbers:
    for i in range(len(Q)):
        strike = 0
        ball = 0

        for j in range(3):
            if str(num[j]) == str(Q[i][0])[j] :
                strike +=1
            elif str(Q[i][0])[j] in str(num):
                ball+=1
        
        if strike != Q[i][1] or ball != Q[i][2]:
            break

        if i == (len(Q)-1):
            result+=1

print(result)