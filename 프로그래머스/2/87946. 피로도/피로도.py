from itertools import permutations

def solution(k, dungeons):
    max_cnt = 0
    for p in permutations(dungeons):
        cnt, k_tmp = 0, k
        for need, pay in p:
            if k_tmp >= need :
                k_tmp -= pay
                cnt += 1
        if cnt > max_cnt : 
            max_cnt = cnt

    return max_cnt