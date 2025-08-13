def solution(str1, str2):
    answer=0
    set1=[]
    set2=[]

    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            set1.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            set2.append(str2[i:i+2].lower())
    
    union=set(set1)|set(set2)
    
    x=[] 
    y=[]
    
    if union:
        for u in union:
            x.extend([u]*min(set1.count(u),set2.count(u)))
            y.extend([u]*max(set1.count(u),set2.count(u)))
        
        answer=int(len(x)/len(y)*65536)
        return answer
    else:
        return 65536