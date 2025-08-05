import heapq

def dijkstra(start, graph, n):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distance[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            dist = current_dist + weight
            if dist < distance[neighbor]:
                distance[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))

    return distance

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    from_s = dijkstra(s, graph, n)
    from_a = dijkstra(a, graph, n)
    from_b = dijkstra(b, graph, n)

    answer = float('inf')
    for k in range(1, n + 1):
        total = from_s[k] + from_a[k] + from_b[k]
        answer = min(answer, total)

    return answer
