def solution(today, terms, privacies):
    answer = []
    i=1
    n_terms=[]
    n_periods=[]
    for t in terms:
        term, period = t.split(" ")
        n_terms.append(term)
        n_periods.append(int(period))

        
    for p in privacies:
        date, term = p.split(" ")
        period = n_periods[n_terms.index(term)]

        year, month, day = map(int, date.split("."))
        month+=period
    
        if month>=13:
            if month%12==0:
                year+=(month//12)
                year-=1
                month=12
            else:
                year+=(month//12)
                month%=12
        
        t_year, t_month, t_day = map(int, today.split("."))

        if year < t_year:
            answer.append(i)
        elif year == t_year and month<t_month:
            answer.append(i)
        elif year == t_year and month==t_month and day<=t_day:
            answer.append(i)
            
        i+=1
    return answer