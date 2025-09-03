def solution(data, ext, val_ext, sort_by):
    answer = []
    columns=['code', 'date','maximum','remain']
    n=columns.index(ext)
    for d in data:
        if d[n]<=val_ext:
            answer.append(d)
    s = columns.index(sort_by)
    answer.sort(key=lambda x: (x[s]))
    return answer