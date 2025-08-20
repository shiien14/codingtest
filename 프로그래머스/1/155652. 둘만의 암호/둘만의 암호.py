def solution(s, skip, index):
    answer=""
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for ch in skip:
        alpha.remove(ch)
        
    n=len(alpha)
    
    for c in s:
        a = alpha.index(c)+index
        if a>=n:
            a%=n
        answer+=alpha[a]
    return answer