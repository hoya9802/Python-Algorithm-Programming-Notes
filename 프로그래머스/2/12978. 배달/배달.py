import heapq

def solution(N, road, K):
    INF = int(1e9)
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    
    for r in road:
        a, b, c = r
        graph[a].append((b,c)); graph[b].append((a,c))
    
    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    dijkstra(1)
    return sum(1 for x in distance[1:] if x <= K)