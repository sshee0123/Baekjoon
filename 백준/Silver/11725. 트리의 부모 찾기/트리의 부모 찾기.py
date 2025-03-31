import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
visited = [False] * (n+1) # 방문확인리스트
parent = [0] * (n+1)    # 부모리스트
# tree 인접리스트로 생성
graph = [[] for _ in range(n+1)]
for _ in range(1,n):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

# dfs
def dfs(n):
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            parent[i] = n
            dfs(i)

dfs(1) # 루트노드(1) 부터
for i in range(2,n+1):
    print(parent[i])