def solution(citations):
    answer=0
    cnt=0
    n=len(citations)
    citations.sort()
    for i in range(n):
        cnt=n-i
        answer = max(min(cnt,citations[i]),answer)
    return answer