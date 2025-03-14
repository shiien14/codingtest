import sys

input = sys.stdin.readline

scores=[]

for i in range(8):
    scores.append([int(input()),i+1])

scores.sort(reverse=True)


num = []
result=0

for i in range(5):
    result += scores[i][0]
    num.append(scores[i][1])

print(result)
print(*sorted(num)) 