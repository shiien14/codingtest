def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    now_m , now_s=map(int,pos.split(":"))
    end_m , end_s=map(int,video_len.split(":"))
    op_s_m, op_s_s=map(int,op_start.split(":"))
    op_e_m, op_e_s=map(int,op_end.split(":"))
    for c in commands:
        if op_s_m*60+op_s_s<=now_m*60+now_s<=op_e_m*60+op_e_s:
            now_m=op_e_m
            now_s=op_e_s
        if c =='prev':
            now_s -= 10
            if now_s < 0:
                if now_m >0:
                    now_m-=1
                    now_s+=60
                else:
                    now_s=0
        elif c =='next':
            now_s += 10
            if now_s>=60:
                now_m+=now_s//60
                now_s%=60
            if now_m >= end_m and now_s > end_s:
                now_m = end_m
                now_s = end_s

    if op_s_m*60+op_s_s<=now_m*60+now_s<=op_e_m*60+op_e_s:
        now_m=op_e_m
        now_s=op_e_s

    answer = str(now_m).zfill(2)+":"+str(now_s).zfill(2)
    return answer