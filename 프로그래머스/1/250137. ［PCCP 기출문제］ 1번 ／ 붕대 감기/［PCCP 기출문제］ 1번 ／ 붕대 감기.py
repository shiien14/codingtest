def solution(bandage, health, attacks):
    time = bandage[0]
    re = bandage[1]
    add_re = bandage[2]
    max_h = health

    success=0
    j=0
    for i in range(1,attacks[-1][0]+1):
        if i==attacks[j][0]:
            health -= attacks[j][1]
            j+=1
            success=0
            if health<=0:
                return -1
        else:
            success+=1
            health+=re
            if time == success:
                health+=add_re
                success=0
            if health>max_h:
                health=max_h
    return health