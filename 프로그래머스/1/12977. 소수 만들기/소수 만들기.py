from itertools import combinations
def solution(nums):
    answer = 0

    result=[]
    for com in list(combinations(nums, 3)):
        n=sum(com)
        answer+=1
        flag=1
        for i in range(2, int(n**0.5)+1):
            j=2
            while i*j <= n:
                if i*j == n:
                    flag=0
                    break
                j+=1
            if flag==0:
                answer-=1
                break

    return answer