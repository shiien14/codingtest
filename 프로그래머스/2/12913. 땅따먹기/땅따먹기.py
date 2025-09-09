from copy import deepcopy
def solution(land):
    answer = deepcopy(land)

    for i in range(1,len(land)):
        for j in range(len(land[i])):
            for k in range(len(land[i])):
                if j==k:
                    continue
                else:
                    answer[i][k]=max(answer[i][k], answer[i-1][j]+land[i][k])
        
    return max(answer[-1])