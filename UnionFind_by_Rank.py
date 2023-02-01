parent = []
rank = []

def init(n):
    for i in range(1,n+1):
        parent[i] = i
        rank[i] = 1

def find(v):
    if v == parent[v]:
        return v
    return find(parent[v])

def merge(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return
    if rank[u] > rank[v]:
        u,v = v,u
    parent[u] = v
    if rank[u] == rank[v]:
        rank[v] += 1
        