import sys

input = sys.stdin.readline

mm=['a','e','i','o','u']
allow=['e','o']

while True:
    command = input().strip()
    if command == 'end':
        break
    cnt=0
    mm_cnt=0
    nm_cnt=0
    mm_ok=0
    ok=1
    if len(command)==1:
        if command[0] in mm:
            print('<'+command+"> is acceptable.")
        else:
            print('<'+command+"> is not acceptable.")
    else:
        for i in range(len(command)-1):
            if command[i] in mm:
                mm_ok +=1
            if command[i] == command[i+1]:
                if command[i] in allow and cnt<2:
                    cnt+=1
                else:
                    ok=0
            else:
                cnt=0
            if command[i] in mm:
                nm_cnt=0
                mm_cnt+=1
            elif command[i] not in mm:
                nm_cnt+=1
                mm_cnt=0
            
            if nm_cnt>2 or mm_cnt>2:
                ok=0

        if command[-1] in mm:
            nm_cnt=0
            mm_cnt+=1
            mm_ok +=1
        elif command[-1] not in mm:
            nm_cnt+=1
            mm_cnt=0
        
        if nm_cnt>2 or mm_cnt>2:
            ok=0
        
        if mm_ok>0 and ok>0:
            print('<'+command+"> is acceptable.")
        else:
            print('<'+command+"> is not acceptable.")