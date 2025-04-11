import sys

input = sys.stdin.readline

N = int(input())
sum = 1
cnt = 1
start_index=1
end_index=1

while end_index != N :
    if sum>N:
        sum-=start_index
        start_index+=1
    elif sum < N:
        end_index+=1
        sum+=end_index
    elif sum == N:
        cnt+=1
        end_index+=1
        sum+=end_index

print(cnt)