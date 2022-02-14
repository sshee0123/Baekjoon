from collections import deque

n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph,v,visited):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = visited[v]+1
            dfs(graph,i,visited)

def bfs(graph,v,visited):
    q = deque()
    q.append(v)
    while q:
        p = q.popleft()
        # print(p)
        for i in graph[p]:
            if not visited[i]:
                visited[i] = visited[p]+1
                q.append(i)
bfs(graph,a,visited)
# dfs(graph,a,visited)
if visited[b]>0:
    print(visited[b])
else:
    print(-1)
