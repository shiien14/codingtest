import sys

input = sys.stdin.readline

map1=[]
for _ in range(9):
    map1.append(list(map(int,input().split())))

max_num=0
index_i,index_j=0,0

for i in range(9):
    for j in range(9):
        if map1[i][j]>max_num:
            index_i, index_j=i,j
            max_num=map1[i][j]

print(max_num)
print(index_i+1, index_j+1)