from collections import Counter
def solution(want, number, discount):
    answer = 0
    lists = list(zip(want, number))
    
    for i in range(len(discount)-9):
        answer+=1
        count=Counter(discount[i:i+10])
        for name, cnt in lists:
            if cnt != count[name]:
                answer-=1
                break
    
    return answer