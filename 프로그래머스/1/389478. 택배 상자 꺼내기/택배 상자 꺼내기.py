def solution(n, w, num):
    total  = (n + w - 1) // w    
    target = (num + w - 1) // w    
    n_rem  = n % w or w               
    t_rem  = num % w or w

    res = 1
    
    if total % 2 == target % 2 and n_rem < t_rem:
        res -= 1


    if total % 2 != target % 2 and n_rem + t_rem <= w:
        res -= 1

    return (total - target) + res