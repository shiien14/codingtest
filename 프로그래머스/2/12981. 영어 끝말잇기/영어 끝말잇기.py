def solution(n, words):
    answer = []

    count = [1]*n
    used=[]
    alpha=words[0][0]
    for i in range(len(words)):
        if words[i] not in used and words[i][0]==alpha:
            used.append(words[i])
            count[i%n]+=1
            alpha = words[i][-1]
        elif words[i] in used or words[i][0]!=alpha:
            return i%n+1, count[i%n]
    return 0,0
        
    