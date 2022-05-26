import sys
sys.setrecursionlimit(10**9)
from collections import deque
T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx,ny)

def bfs(graph,x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            # if nx<0 or nx>=M or ny<0 or ny>=N:
            #     continue
            if 0<=nx<M and 0<=ny<N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))

for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0]*N for _ in range(M)]
    result = 0

    for _ in range(K):
        a,b = map(int,input().split())
        graph[a][b] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] ==1:
                bfs(graph,i,j)
                result+=1
    print(result)
