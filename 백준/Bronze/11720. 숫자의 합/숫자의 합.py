import sys

input= sys.stdin.readline

N = int(input())
nums = input()
answer=0

for i in range(N):
    answer+=int(nums[i])

print(answer)