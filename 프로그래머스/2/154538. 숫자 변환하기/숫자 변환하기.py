def solution(x, y, n):
    answer = 0
    case = set([x])
    
    while case:
        if y in case:
            return answer
        
        tmp = set()
        for num in case:
            plus = num + n
            mul2 = num * 2
            mul3 = num * 3
            
            if plus <= y:
                tmp.add(plus)
            if mul2 <= y:
                tmp.add(mul2)
            if mul3 <= y:
                tmp.add(mul3)
        case = tmp
        answer += 1
    
    return -1