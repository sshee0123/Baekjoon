import sys
input = sys.stdin.readline

n = int(input()) # 사람수
a,b = map(int,input().split()) # 구해야하는 두사람 번호
m = int(input()) # 관계 수
graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph)

visited = [False]*(n+1)
def dfs(graph,v,visited):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = visited[v] + 1
            dfs(graph,i,visited)
dfs(graph,a,visited)
# print(a,visited)
if not visited[b]:
    print(-1)
else:
    print(visited[b])
