import sys
input = sys.stdin.readline

N = int(input().strip())
paper = [list(map(int, input().split())) for _ in range(N)]

result = [0,0,0]

def check(x,y, n):
    value = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != value:
                return None
    return value

def divide(x, y, n):
    v = check(x,y,n)
    if v is not None:
        if v == -1:
            result[0] += 1
        elif v == 0:
            result[1] += 1
        else:
            result[2] += 1
    else:
        size = n//3
        for i in range(3):
            for j in range(3):
                divide(x+i*size, y+j*size, size)
                
                
divide(0,0,N)

print(result[0])
print(result[1])
print(result[2])