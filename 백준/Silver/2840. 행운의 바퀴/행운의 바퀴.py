import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
result = ['?']*n
index=0
for _ in range(k):
    num, alpha = input().split()
    index+=int(num)
    if result[index%n] == '?' and alpha not in result:
        result[index%n]=alpha
    elif result[index%n]==alpha:
        continue
    else:
        print('!')
        exit()

print(''.join(result[(index - i) % n] for i in range(n)))