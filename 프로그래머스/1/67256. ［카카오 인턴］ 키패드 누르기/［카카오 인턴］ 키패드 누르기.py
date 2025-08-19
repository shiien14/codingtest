def solution(numbers, hand):
    pos = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    left_keys  = {1,4,7}
    right_keys = {3,6,9}

    left  = '*' 
    right = '#'
    answer = ''

    for n in numbers:
        if n in left_keys:
            answer+='L'
            left = n
        elif n in right_keys:
            answer+='R'
            right = n
        else:
            dl = abs(pos[left][0] - pos[n][0]) + abs(pos[left][1] - pos[n][1])
            dr = abs(pos[right][0] - pos[n][0]) + abs(pos[right][1] - pos[n][1])

            if dl < dr or (dl == dr and hand == 'left'):
                answer+='L'
                left = n
            else:
                answer+='R'
                right = n

    return answer
