import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*100001
dp2 = [0] *100001
for i in range(n):
    dp[i+1]=int(input())


dp2[1] = dp[1]
dp2[2] = dp2[1]+dp[2]
#1과 2는 연속으로 마신 값이기 때문에 초기값 설정

#1 - OXO -2 위치의 최대값을 더한 경우dp[i]+dp2[i-2]
#2 - XOO -3위치 최대값에서 하나 건너 뛴 경우dp[i]+dp[i-1]+dp2[i-3]
#3 - OOX -1의 최대값 dp2[i-1]

for i in range(3,n+1):
    dp2[i]=max(dp2[i-1], dp[i] + dp2[i-2], dp[i] + dp[i-1] + dp2[i-3])
print(dp2[n])