def solution(dirs):
    answer = 0
    d = {'U':(1,0), 'D':(-1,0), 'R':(0,1), 'L':(0,-1)}
    
    x,y= 0,0
    result=[]
    for i in range(len(dirs)):
        dx,dy= d[dirs[i]][0], d[dirs[i]][1]
        nx = x + dx
        ny = y + dy
        if -5<=nx<=5 and -5<=ny<=5:
            if [(x,y),(nx,ny)] not in result:
                answer+=1
                result.append([(x,y),(nx,ny)])
                result.append([(nx,ny), (x,y)])
            x, y = nx, ny
        
    return answer