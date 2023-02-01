# def find(x):
#     # 루트 노드를 찾을 때 까지 재귀 호출
#     if root[x] != x:
#         return find(root[x])
#     return x

def find(x):
    # 루트 노드를 찾을 때 까지 재귀 호출
    if root[x] != x:
        # 경로 압축
        root[x] = find(root[x])
    return root[x]
    
def union(x, y):
    x = find(x)
    y = find(y)
    
    # 더 작은 루트노드에 합친다.
    if x < y:
        root[y] = x
    else:
        root[x] = y


if __name__ == "__main__":
    SIZE = 8
    root = list(range(SIZE+1))
    print(root[1], root[2])
    union(1, 2)
    print(root)
    print(root[2], root[3])
    union(2, 3)
    print(root)
    print(root[4], root[5])
    union(4, 5)
    print(root)
    print(root[4], root[6])
    union(4, 6)
    print(root)
    print(root[6], root[7])
    union(6, 7)
    print(root)