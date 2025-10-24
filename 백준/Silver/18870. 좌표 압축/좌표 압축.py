import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
s_nums = list(sorted(set(nums)))

dic = dict()
for i in range(len(s_nums)):
    dic[s_nums[i]]=i

for num in nums:
    print(dic[num],end=" ")