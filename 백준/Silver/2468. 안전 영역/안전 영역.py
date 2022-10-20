from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
max_h = 0
result = 0
for i in range(n):
    tmp = max(graph[i])
    max_h = max(tmp, max_h)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
def bfs(a, b, visited, h):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] > h and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = 1
for h in range(max_h):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                bfs(i, j, visited, h)
                cnt += 1
    if result < cnt : 
        result = cnt
print(result)