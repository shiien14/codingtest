def solution(elements):
    answer = set()
    elements2=elements*2
    for n in range(1,len(elements)+1):
        for i in range(len(elements)):
            answer.add(sum(elements2[i:i+n]))
    return len(answer)