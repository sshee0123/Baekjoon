N = int(input())
M = int(input())
graph = [[]*N for _ in range(N+1)]

for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0]*(N+1)
answer = 0
def dfs(graph, v, visited):
    global answer
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            answer+=1
dfs(graph,1,visited)
print(answer)