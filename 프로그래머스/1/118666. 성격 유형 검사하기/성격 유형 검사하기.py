def solution(survey, choices):
    answer = ''
    scores = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    n=len(survey)
    
    for i in range(n):
        if choices[i] > 4:
            scores[survey[i][1]]+=(choices[i]-4)
        else:
            scores[survey[i][0]]+=(4-choices[i])

    if scores['R'] < scores['T']:
        answer+='T'
    else:
        answer+='R'
    if scores['C'] < scores['F']:
        answer+='F'
    else:
        answer+='C'
    if scores['J'] < scores['M']:
        answer+='M'
    else:
        answer+='J'
    if scores['A'] < scores['N']:
        answer+='N'
    else:
        answer+='A'

    return answer