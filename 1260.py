from collections import deque

N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    m1, m2 = map(int,input().split())
    graph[m1].append(m2)
    graph[m2].append(m1)

#정렬 해야하
for i in range(N+1):
    graph[i].sort()

visited = [False]*(N+1)

def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,v,visited):
    q = deque([v])
    visited[v] = True
    while q:
        s = q.popleft()
        print(s,end = ' ')
        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(graph,V,visited)
visited = [False]*(N+1)
print()
bfs(graph,V,visited)

