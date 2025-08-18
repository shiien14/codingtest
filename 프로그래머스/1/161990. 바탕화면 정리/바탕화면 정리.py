def solution(wallpaper):
    answer = []
    lux,luy,rdx,rdy=50,50,0,0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=="#":
                if lux>i:
                    lux=i
                if luy>j:
                    luy=j
                if rdx<=i:
                    rdx=i+1
                if rdy<=j:
                    rdy=j+1
    return [lux,luy,rdx,rdy]