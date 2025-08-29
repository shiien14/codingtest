from collections import Counter
def solution(X, Y):
    answer = ''
    x_cnt = Counter(X)
    y_cnt = Counter(Y)
    common= (x_cnt & y_cnt)
    
    sorted_com= sorted(common, reverse=True)
    
    if len(common)==0:
        return "-1"
    
    for sc in sorted_com:
        re=common[sc]
        answer+=(sc*re)
    
    if answer[0] == "0":
        return "0"
    else:
        return answer