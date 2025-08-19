from collections import Counter
def solution(participant, completion):
    p=Counter(participant)
    c=Counter(completion)
    
    for k in p:
        if k in c:
            c[k]-=p[k]
            if c[k]<0:
                return k
        else:
            return k