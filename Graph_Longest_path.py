# LongestPath

ve = [
    [1,0],
    [3,2],
    [1,2],
    [3,2]
]
n = 2



T = n
for t in range(T):
    vertex, edge = ve[t][0], ve[t][1]
    graph = [[] for _ in range(vertex + 1)]
    for i in range(edge):
        a, b = ve[i][0], ve[i][1]
        graph[a].append(b)
        graph[b].append(a)
    result = 0
    for i in range(1, vertex + 1):
        visited = [False] * (vertex + 1)
        def dfs(v, count):
            global result
            visited[v] = True
            result = max(result, count)
            for x in graph[v]:
                if not visited[x]:
                    dfs(x, count+1)
                    visited[x] = False
        dfs(i, 1)
    print(t+1, result)


