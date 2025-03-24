import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y: # 문자열 같으면 리턴
        return network[x]
    # 부모노드 변경하고 네트워크 수 늘이긱®
    parent[y] = x
    network[x] += network[y]
    return network[x]

t = int(input())
for _ in range(t):
    parent = dict() # 부모 노드
    network = dict() # 친구 수 (네트워크 수)
    f = int(input())
    for _ in range(f):
        a,b = input().split()
        if not network.get(a):
            parent[a] = a
            network[a] = 1
        if not network.get(b):
            parent[b] = b
            network[b] = 1
        # print("before parent", parent)
        # print("before networkd", network)
        print(union(a,b))
        # print("after parent", parent)
        # print("after networkd", network)
