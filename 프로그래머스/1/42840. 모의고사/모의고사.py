def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    n1 = len(answers)//len(s1)
    n2 = len(answers)//len(s2)
    n3 = len(answers)//len(s3)
    
    cnt1=0
    cnt2=0
    cnt3=0
    s1=s1*(n1+1)
    s2=s2*(n2+1)
    s3=s3*(n3+1)
    for i in range(len(answers)):
        if answers[i] == s1[i]:
            cnt1+=1
        if answers[i] == s2[i]:
            cnt2+=1
        if answers[i] == s3[i]:
            cnt3+=1
    answer=[]
    m_cnt=max(cnt1,cnt2,cnt3)
    if m_cnt==cnt1:
        answer.append(1)
    if m_cnt==cnt2:
        answer.append(2)
    if m_cnt==cnt3:
        answer.append(3)
    
    return answer