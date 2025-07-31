from collections import defaultdict

def solution(clothes):
    d = defaultdict(int)
    
    for name, ca in clothes:
        d[ca]+=1
        
    answer=1
    for num in d.values():
        answer*=(num+1)
        
    return answer-1