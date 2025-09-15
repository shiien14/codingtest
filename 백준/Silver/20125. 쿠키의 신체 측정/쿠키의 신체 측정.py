import sys
input = sys.stdin.readline

n = int(input())
cookie = [input().strip() for _ in range(n)]

heart = None
for i in range(n):
    if '*' in cookie[i]:
        y = cookie[i].index('*')
        heart = [i + 2, y + 1]
        break

x, y = heart
x -= 1
y -= 1

l_a = r_a = w = l_l = r_l = 0

for j in range(y - 1, -1, -1):
    if cookie[x][j] == '_': break
    if cookie[x][j] == '*': l_a += 1

for j in range(y + 1, n):
    if cookie[x][j] == '_': break
    if cookie[x][j] == '*': r_a += 1

for i in range(x + 1, n):
    if cookie[i][y] == '_': break
    if cookie[i][y] == '*': w += 1

start = x + w + 1
for i in range(start, n):
    if cookie[i][y - 1] == '_': break
    if cookie[i][y - 1] == '*': l_l += 1

for i in range(start, n):
    if cookie[i][y + 1] == '_': break
    if cookie[i][y + 1] == '*': r_l += 1

print(heart[0], heart[1])
print(l_a, r_a, w, l_l, r_l)
