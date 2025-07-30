def solution(number, limit, power):
    answer = 0
    attacks=[1]
    for n in range(2,number+1):
        cnt=0
        for i in range(1, int(n**0.5)+1):
            if n%i==0:
                if i**2==n:
                    cnt+=1
                else:
                    cnt+=2
        attacks.append(cnt)
    for a in attacks:
        if a>limit:
            answer+=power
        else:
            answer+=a
    return answer