def dfs(n, computers, visited, v):
    print("dfs 호출" ,v)
    visited[v] = True
    for i in range(n):
        if computers[v][i] == 1 and v!=i: # 컴퓨터가 연결되어있고 v가 자기 자신이 아니면
            if not visited[i]:
                dfs(n, computers, visited, i)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, visited, i)
            answer += 1
    return answer