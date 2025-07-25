def solution(a, b, n):
    answer = 0
    
    while n>=a:
        num = n//a
        n=n%a
        n += num*b
        answer+=num*b
    
    return answer