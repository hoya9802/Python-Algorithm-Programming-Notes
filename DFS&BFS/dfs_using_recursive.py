graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

def dfs(graph, v):
    print(v, end= " ")
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i)

dfs(graph, 1)

# 1 2 7 6 8 3 4 5
