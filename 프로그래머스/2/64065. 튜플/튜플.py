def solution(s):
    answer=[]
    par=list(s.split("{"))
    result = []
    
    for p in par:
        if p != "":
            result.append(p.split("}")[0])   

    result.sort(key = lambda x : len(x))
    
    for r in result:
        for a in map(int,r.split(',')):
            if a not in answer:
                answer.append(a)
    return answer