import heapq  # 우선순위 큐 구현을 위함


def dijkstra(graph, start, visited):
  distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
  distances[start] = 0  # 시작 값은 0이어야 함
  print('distances->', distances)
  queue = []
  heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.
  print('queue->', queue)

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    # 탐색 할 노드, 거리를 가져옴.
    print('queue->', queue)
    current_distance, current_destination = heapq.heappop(queue)
    
    # print('current_destination---->', current_destination)
    # if current_destination not in visited:
    #   visited.append(current_destination)
    # else:
    #   return distances[current_destination]

    if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      continue

    for new_destination, new_distance in graph[current_destination].items():
      distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
      if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
        distances[new_destination] = distance
        # 다음 인접 거리를 계산 하기 위해 큐에 삽입
        heapq.heappush(queue, [distance, new_destination])

  return distances


# graph = {
#     'A': {'B':8, 'C':2, 'D':3},
#     'B':{},
#     'C':{'B':3, 'D':2},
#     'D':{'E':1, 'F':4},
#     'E':{},
#     'F':{}
# }
# print(dijkstra(graph, 'A'))


# arr = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
arr = [[1,2,1],[2,1,3]]
n = 2
k = 2
graph_d = {}
visited = []

for i in range(n):
    graph_d[i+1] = {}

for i, j, x in arr:
    tmp = graph_d[i]
    
    tmp[j] = x
    graph_d[i] = tmp

print(graph_d)
print(dijkstra(graph_d, k, visited))