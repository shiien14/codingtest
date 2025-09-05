def solution(park, routes):
    n=len(park)
    m=len(park[0])
    for i in range(n):
        if 'S' in park[i]:
            start_i= i
            start_j= park[i].index('S')
            break
    i=start_i
    j=start_j
    for r in routes:
        d, index = r.split(" ")
        if d =='N':
            tmp=i
            for k in range(int(index)):
                i-=1
                if 0<=i<n:
                    if park[i][j]=='X':
                        i=tmp
                        break
                else:
                    i=tmp
                    break
        elif d=='S':
            tmp=i
            for k in range(int(index)):
                i+=1
                if 0<=i<m:
                    if park[i][j]=='X':
                        i=tmp
                        break
                else:
                    i=tmp
                    break
        elif d=='W':
            tmp=j
            for k in range(int(index)):
                j-=1
                if 0<=j<n:
                    if park[i][j]=='X':
                        j=tmp
                        break
                else:
                    j=tmp
                    break
        elif d=='E':
            tmp=j
            for k in range(int(index)):
                j+=1
                if 0<=j<m:
                    if park[i][j]=='X':
                        j=tmp
                        break
                else:
                    j=tmp
                    break
            
    return [i,j]