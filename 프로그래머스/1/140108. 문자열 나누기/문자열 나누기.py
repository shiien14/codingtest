def solution(s):
    answer = 1
    x=s[0]
    cnt1,cnt2=0,0
    for let in s:
        if cnt1!=0 and cnt1==cnt2:
            answer+=1
            cnt1=0
            cnt2=0
            x=let
        if let==x:
            cnt1+=1
        elif let!=x:
            cnt2+=1
    return answer