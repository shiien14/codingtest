import sys

input = sys.stdin.readline

nums = input().strip()
count1,count0=0,0

for n in nums:
    if n == '1':
        count1+=1
    else:
        count0+=1
    
count0//=2
count1//=2

answer = '0'*count0 +'1'*count1
print(answer)