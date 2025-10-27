import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
tmp = [0]
result = []
now_sum = 0

for i in range(n):
  now_sum += nums[i]
  tmp.append(now_sum)


for i in range(n-m+1):
  result.append(tmp[i+m] - tmp[i])

print(max(result))