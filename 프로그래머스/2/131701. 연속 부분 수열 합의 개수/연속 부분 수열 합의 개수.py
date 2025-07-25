def solution(elements):
    answer = []
    elements2=elements*2
    for n in range(1,len(elements)+1):
        for i in range(0,len(elements2)):
            answer.append(sum(elements2[i:i+n]))
    return len(set(answer))