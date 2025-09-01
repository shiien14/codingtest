def solution(keymap, targets):
    answer = []
    for tar in targets:
        result=0
        for t in tar:
            cnt=102
            for k in keymap:
                if t in k:
                    if cnt > k.find(t):
                        cnt = k.find(t)
            if cnt == 102:
                result=-1
                break
            else:
                result+=cnt+1
        answer.append(result)
            
    return answer