import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())
# 1~N 까지의 양방향 간선 (더 작은 정점부터 방문 -> 정렬)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in range(n+1):
    graph[i].sort()
    
visited = [False] * (n+1)

def dfs(graph,v,visited):
    visited[v] = True
    print(v,end = " ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

q = deque()
def bfs(graph,v,visited):
    q.append(v)
    visited[v] = True
    while q:
        s = q.popleft()
        print(s,end=" ")
        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(graph,v,visited)
visited = [False] * (n+1)
print()
bfs(graph,v,visited)
