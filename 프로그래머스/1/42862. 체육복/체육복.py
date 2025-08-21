def solution(n, lost, reserve):
    answer = 0
    result = [1]*(n+1)
    result[-1]=0
    lost.sort()
    reserve.sort()
    
    for r in reserve:
        if r in lost:
            lost.remove(r)
            continue
        result[r-1]+=1

    for l in lost:
        result[l-1]-=1
        if result[l-1]==0:
            if result[l-2]>1 :
                result[l-2]-=1
                result[l-1]+=1
            
            elif result[l]>1:
                result[l]-=1
                result[l-1]+=1

    return n-result.count(0)+1