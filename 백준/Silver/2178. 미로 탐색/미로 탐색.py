import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()
q.append((0,0))
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx,ny))
print(graph[n-1][m-1])

