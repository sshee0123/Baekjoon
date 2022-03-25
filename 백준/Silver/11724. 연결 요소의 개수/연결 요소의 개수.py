# 11724
import sys
sys.setrecursionlimit(10000)

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph)

def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            dfs(i)
            
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)