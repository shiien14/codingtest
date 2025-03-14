import sys

input = sys.stdin.readline

N, M = map(int, input().split())

prices12=[]
prices6=[]

for i in range(M):
    a,b=map(int, input().split())
    prices12.append(a)
    prices6.append(b)

prices12.sort()
prices6.sort()


result1=(N//6+1)*prices12[0]
result2=(N//6*prices12[0])+(N%6*prices6[0])
result3=N*prices6[0]

print(min(result1,result2,result3))