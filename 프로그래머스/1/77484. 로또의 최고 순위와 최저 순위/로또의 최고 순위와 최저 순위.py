def solution(lottos, win_nums):
    answer = []
    cnt=0
    for l in lottos:
        if l in win_nums:
            cnt+=1
    miss = lottos.count(0)

    if (cnt+miss)>1:
        answer.append(7-(cnt+miss))
    else:
        answer.append(6)
        
    if cnt>1:
        answer.append(7-cnt)
    else:
        answer.append(6)

    return answer