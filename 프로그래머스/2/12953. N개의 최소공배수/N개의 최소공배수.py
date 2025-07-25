def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)

def solution(arr):
    for i in range(1,len(arr)):
        num=gcd(arr[i-1], arr[i])
        lcm = arr[i-1]*arr[i]//num
        arr[i]=lcm
    
    return lcm