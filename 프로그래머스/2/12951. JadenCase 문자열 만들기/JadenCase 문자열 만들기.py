def solution(s):
    answer = []
    words=s.split(' ')
    for i in words:
        i=i.lower()
        i=i.capitalize()
        answer.append(i)
    return ' '.join(answer)