from collections import Counter
def solution(k, tangerine):
    answer=1
    cnt = Counter(tangerine)
    result = list(sorted(cnt.values()))
    
    msum=0
    for i in range(len(result)-1, -1, -1):
        msum+=result[i]
        if msum>=k:
            return answer
        answer+=1
    return answer
