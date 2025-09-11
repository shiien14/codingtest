import sys

input= sys.stdin.readline

n, k = map(int, input().split())

countries = []
for i in range(n):
    country, gold, silver, bronze = map(int, input().split())
    sum=gold*3+silver*2+bronze
    countries.append([sum, country])

countries.sort(reverse=True)

countries[0].append(1)
cnt=1
for i in range(1, n):
    cnt+=1
    if countries[i][0] == countries[i-1][0]:
        countries[i].append(countries[i-1][-1])
    else:
        countries[i].append(cnt)
    if countries[i][1] == k:
        print(countries[i][-1])
        break
    