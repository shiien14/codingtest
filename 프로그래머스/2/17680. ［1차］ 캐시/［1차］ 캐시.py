def solution(cacheSize, cities):
    answer = 0
    time = 0 
    cache = []
    
    if cacheSize==0:
        return len(cities)*5
    
    for c in cities:
        c=c.lower()
        if c in cache:
            time += 1
            cache.remove(c)
            cache.append(c)
        else:
            if len(cache)==cacheSize:
                cache.remove(cache[0])
                cache.append(c)
            else:
                cache.append(c)
            time+=5
    return time