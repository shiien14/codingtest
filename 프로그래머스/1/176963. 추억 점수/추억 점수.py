def solution(name, yearning, photo):
    answer = []
    info = list(zip(name, yearning))

    for p in photo:
        score=0
        for name, yearn in info:
            if name in p:
                score+=yearn
        answer.append(score)
    return answer