def solution(schedules, timelogs, startday):
    answer = len(schedules)
    for i in range(len(schedules)):
        time = schedules[i]+10
        if (schedules[i]+10)%100>=60:
            time = schedules[i]-(schedules[i])%100+100 + (schedules[i]+10)%100%60
        for j in range(len(timelogs[i])):
            if ((startday+j) % 7 != 6) and ((startday+j) % 7 != 0):
                if timelogs[i][j]>time:
                    answer-=1
                    break
    return answer