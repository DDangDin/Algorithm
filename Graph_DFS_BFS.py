# use deque(in collections) is more faster

def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


def dfs(graph, start_node):
    visit = list()
    stack = list()
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node]) # 오른쪽부터 순회
            # stack.extend(reversed(graph[node])) # 왼쪽부터 순횐

    return visit

# dfs 시간 문제 때문에 visited 공간 미리 할당하는 코드
# leetcode(1971)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False] * n
        graph = {}
        
        for k,v in edges:
            if k not in graph:
                graph[k] = [v]
            else:
                graph[k].append(v)
            if v not in graph:
                graph[v] = [k]
            else:
                graph[v].append(k)
                
        # print(graph)
                
        def dfs(graph, src, dest, visited):
            node = []
            stack = list()
            stack.append(src)
            
            while stack:
                node = stack.pop()
                if visited[node] == False:
                    visited[node] = True
                    if node in graph:
                        stack.extend(graph[node])
                        
                if visited[dest]==True:
                    return True
                
            return False
                
                        
        result = dfs(graph, source, destination, visited)
        return result


if __name__ == '__main__':
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(bfs(graph, 'G'))
    print(dfs(graph, 'G'))