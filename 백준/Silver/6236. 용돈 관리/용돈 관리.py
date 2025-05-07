import sys

input = sys.stdin.readline

n, m = map(int, input().split())

money=[]
for _ in range(n):
    money.append(int(input()))

start, end = min(money), sum(money)
result=0

while start <= end:
    mid = (start + end) //2
    imsi = mid
    cnt=1

    for mon in money:
        if imsi < mon :
            imsi=mid
            cnt += 1

        imsi -= mon

    if cnt>m:
        start = mid + 1
    elif mid < max(money):
        start = mid+1
    else:
        end=mid-1
        result=mid

print(result)