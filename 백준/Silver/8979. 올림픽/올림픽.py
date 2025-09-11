import sys

input= sys.stdin.readline

n, k = map(int, input().split())

countries = []
for i in range(n):
    country, gold, silver, bronze = map(int, input().split())
    countries.append([gold, silver, bronze, country])

countries.sort(reverse=True)

countries[0].append(1)

if countries[0][3] == k:
    print(1)
    sys.exit(0)

for i in range(1, n):
    rank_num = i + 1
    if countries[i][0] == countries[i-1][0] and countries[i][1] == countries[i-1][1] and countries[i][2] == countries[i-1][2]:
        countries[i].append(countries[i-1][-1])
    else:
        countries[i].append(rank_num)
    if countries[i][3] == k:
        print(countries[i][-1])
        break
    