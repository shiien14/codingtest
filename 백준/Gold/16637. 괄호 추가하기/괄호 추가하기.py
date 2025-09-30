import sys
from collections import deque

input= sys.stdin.readline

def cal(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

n = int(input())
expression = input().strip()

nums=[]
ops=[] 
for c in expression:
    if c in '+-*':
        ops.append(c)
    else:
        nums.append(int(c))

if not ops:
    print(nums[0])
else:
    q=deque()
    q.append((0, nums[0]))

    ans=-int(1e9)

    while q:
        i, result = q.popleft()
        
        if i == len(ops):
            if result > ans:
                ans = result
            continue

        next = cal(result, ops[i], nums[i + 1])
        q.append((i + 1, next))

        if i + 1 < len(ops):
            temp = cal(nums[i + 1], ops[i + 1], nums[i + 2])
            next2 = cal(result, ops[i], temp)
            q.append((i + 2, next2))

    print(ans)