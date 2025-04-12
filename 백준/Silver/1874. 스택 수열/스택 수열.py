import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

stack = []
num=1
result = ""
for i in range(N):
    if nums[i]>=num:
        while nums[i]>=num:
            stack.append(num)
            num+=1
            result+='+'
        stack.pop()
        result+='-'
    else:
        if stack.pop()> nums[i]:
            print("NO")
            exit()
        else:
            result+='-'

for r in result:
    print(r)