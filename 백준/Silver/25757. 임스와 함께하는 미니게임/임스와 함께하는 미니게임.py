import sys

input= sys.stdin.readline

n, g =  input().split()
name = set([input().strip() for _ in range(int(n))])

if g=='Y':
    people =1
    print(len(name)//people)
elif g=='F':
    people=2
    print(len(name)//people)
else:
    people=3
    print(len(name)//people)
    