def dfs(graph,v,visited):
    visited[v] = True
    for i in range(len(graph)):
        if graph[v][i] == 1:
            if not visited[i]:
                dfs(graph,i,visited)
            
def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            dfs(computers,i,visited)
            answer += 1
    return answer