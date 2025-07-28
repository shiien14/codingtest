def solution(n, left, right):
    answer = []
    # for i in range(1, n+1):
    #     for _ in range(i):
    #         answer.append(i)
    #     for j in range(i+1,n+1):
    #         answer.append(j)
    
    for i in range(left, right+1):
        x,y = i//n, i%n
        value = max(x,y)+1
        answer.append(value)
        
    return answer