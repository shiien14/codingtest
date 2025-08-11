def solution(n):
    array=[[True] for _ in range(n+1)]
    for i in range(2,int(n**0.5)+1):
        if array[i]:
            j=2
            while i*j<=n:
                array[i*j] = False
                j+=1
    return array.count([True])-2