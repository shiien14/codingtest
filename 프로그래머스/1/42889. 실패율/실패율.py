from collections import Counter
def solution(N, stages):
    answer = []
    people = len(stages)
    count = Counter(stages)

    for i in range(1,N+1):
        if people == 0:
            answer.append([0,i])
        else:
            if i not in count:
                count[i]=0
            answer.append([count[i]/people,i])
            people -= count[i]
    answer.sort(key = lambda x : (-x[0],x[1]))

    result=[]
    for i in range(len(answer)):
        result.append(answer[i][1])
    return result