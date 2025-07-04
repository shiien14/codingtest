import sys

input = sys.stdin.readline

money = int(input())
info = list(map(int, input().split()))

j_cash = money
j_buy = 0

for price in info:
    if j_cash >= price:
        buy = j_cash // price
        j_buy += buy
        j_cash -= buy * price

j_profit = j_cash + j_buy * info[-1]

s_cash = money
s_buy = 0
up = 0
down = 0
for i in range(1, len(info)):
    if info[i] > info[i-1]:
        up += 1
        down = 0
    elif info[i] < info[i-1]:
        down += 1
        up = 0
    else:
        up = down = 0
    
    if down >= 3:
        if s_cash >= info[i]:
            buy = s_cash // info[i]
            s_buy += buy
            s_cash -= buy * info[i]
    elif up >= 3:
        s_cash += s_buy * info[i]
        s_buy = 0

s_profit = s_cash + s_buy * info[-1]

if j_profit>s_profit:
    print('BNP')
elif j_profit < s_profit:
    print("TIMING")
else:
    print("SAMESAME")