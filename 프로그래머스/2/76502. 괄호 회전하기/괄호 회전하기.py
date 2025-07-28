def solution(s):
    answer = 0
    n=len(s)
    s=s*2
    for i in range(0,n-1):
        new_s = s[i:i+n]
        while True:
            leng=len(new_s)
            new_s=new_s.replace('[]','')
            new_s=new_s.replace('()','')
            new_s=new_s.replace('{}','')
            
            if len(new_s)==0:
                answer+=1
                break
            if leng == len(new_s):
                break
        
    return answer