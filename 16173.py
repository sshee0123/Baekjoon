from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
visited = [[0]*N for _ in range(N)]

# #dfs
# def dfs(x,y):
#     #종료조건
#     if x<=-1 or x>=N or y<=-1 or y>=N or visited[x][y] == 1:
#         return
#     if graph[x][y] == -1:
#         visited[x][y] = 1
#         return
#     #방문표시
#     visited[x][y] = 1
#     #오른쪽, 아래 이동
#     dfs(x,y+graph[x][y])
#     dfs(x+graph[x][y],y)
#
# dfs(0,0)
#
# if visited[-1][-1] == 1:
#     print("HaruHaru")
# else:
#     print("Hing")

#bfs
dx = [0,1]
dy = [1,0]
def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        if graph[x][y] == -1:
            print("HaruHaru")
            return
        for i in range(2):
            nx = x+dx[i]*graph[x][y]
            ny = y+dy[i]*graph[x][y]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                q.append([nx,ny])
                visited[nx][ny] = 1
    print("Hing")

bfs(0,0)
