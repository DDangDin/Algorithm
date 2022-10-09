import heapq

def ShortestPath(graph, first, last):
    distance = {node:[float('inf'), first] for node in graph}
    distance[first] = [0, first]
    queue = []

    heapq.heappush(queue, [distance[first][0], first])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distance[current_node][0] < current_distance:
            continue

        for next_node, weight in graph[current_node].items():
            total_distance = current_distance + weight

            if total_distance < distance[next_node][0]:
                distance[next_node] = [total_distance, current_node]
                heapq.heappush(queue, [total_distance, next_node])

    path = last
    path_output = last + '->'
    while distance[path][1] != first:
        path_output += distance[path][1] + '->'
        path = distance[path][1]
    path_output += first
    print(path_output)
    return distance



graph = {
    'A': {'B':8, 'C':2, 'D':3},
    'B':{},
    'C':{'B':3, 'D':2},
    'D':{'E':1, 'F':4},
    'E':{},
    'F':{}
}
print(ShortestPath(graph, 'A', 'F'))