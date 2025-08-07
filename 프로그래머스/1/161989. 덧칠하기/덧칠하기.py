def solution(n, m, section):
    wall = [1] * n
    for num in section :
        wall[num-1] = 0

    cnt=0
    for i in range(n):
        if wall[i] == 0 :
            if i+m<n:
                for j in range(i, i+m):
                    wall[j]=1
                cnt+=1
            else:
                for j in range(i,n):
                    wall[j]=1
                cnt+=1
    return cnt