# time complexity: O(V^2)
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (n + 1)
visited = [False] * (n + 1)

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(n):
        if min_value > distance[i] and not visited[i]:
            min_value = distance[i]
            index = i
    return  index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]
    
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print('INFINITY')

"""
input:
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
---------
output:
0
2
3
1
2
4
"""