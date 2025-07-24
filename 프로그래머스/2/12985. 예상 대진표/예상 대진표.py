def solution(n,a,b):
    for i in range(n//2):
        if a%2!=0:
            a+=1
        if b%2!=0:
            b+=1
        a//=2
        b//=2
        if a == b:
            return i+1