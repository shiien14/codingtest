def solution(s):
    answer=[]
    result = s.lstrip('{').rstrip('}').split('},{')

    result.sort(key = len)
    
    for r in result:
        for a in map(int,r.split(',')):
            if a not in answer:
                answer.append(a)
    return answer