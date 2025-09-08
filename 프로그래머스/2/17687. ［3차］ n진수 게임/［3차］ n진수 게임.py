def change(num, ch):
    change_num=''
    while num:
        if num%ch ==10:
            change_num = 'A'+change_num
        elif num%ch ==11:
            change_num = 'B'+change_num
        elif num%ch ==12:
            change_num = 'C'+change_num
        elif num%ch ==13:
            change_num = 'D'+change_num
        elif num%ch ==14:
            change_num = 'E'+change_num
        elif num%ch ==15:
            change_num = 'F'+change_num
        else:
            change_num=str(num%ch)+change_num
        num//=ch
    
    return change_num

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