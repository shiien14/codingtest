import sys

input = sys.stdin.readline

total = input()
sub =total.split('-')

result = sum(map(int, sub[0].split('+')))

for s in sub[1:]:
    result-=sum(map(int, s.split('+')))

print(result)