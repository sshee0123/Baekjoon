import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

max_h = 0 # 지역 최대 높이
for i in range(n):
    tmp = max(graph[i])
    max_h = max(max_h,tmp)

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,h,visited):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            if graph[nx][ny] > h:
                visited[nx][ny] = True
                dfs(nx,ny,h,visited)

def bfs(x,y,h,visited):
    q = deque()
    q.append((x,y))
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny] > h:
                    visited[nx][ny] = True
                    q.append((nx,ny))
result = 0
# 지역 최대 높이만큼 탐색
for h in range(max_h):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for a in range(n):
        for b in range(n):
            if graph[a][b] > h and not visited[a][b]:
                visited[a][b] = True
                cnt += 1
                #dfs(a,b,h,visited)
                bfs(a,b,h,visited)
    result = max(cnt,result)
print(result)