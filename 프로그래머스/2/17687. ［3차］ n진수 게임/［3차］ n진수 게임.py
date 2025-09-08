def change(num, ch):
    total = "0123456789ABCDEF"
    i,j = divmod(num,ch)
    if i ==0:
        return total[j]
    else : 
        return change(i,ch)+total[j]

def solution(n, t, m, p):
    answer = ''
    tmp = '0'
    i=1
    while len(tmp)<m*t:
        tmp+=change(i,n)
        i+=1

    for i in range(p-1,m*t,m):
        answer+=tmp[i]
    
    return answer