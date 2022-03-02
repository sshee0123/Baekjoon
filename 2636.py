import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
# visited = [[0]*m for _ in range(n)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]
result = [] #가장자리 치즈 개수 배열

#bfs
def bfs():
    #bfs돌 때마다 치즈 녹아서 없어지니까 visited 갱신해줘야함
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    cnt = 0 #가장자리 치즈 개수

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #아직 방문 안했다면 상하좌우 이동
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                #치즈 없는 곳이면 이동 가능
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                #치즈 있는 곳이면 가장자리 cnt
                else:
                    visited[nx][ny] = 1
                    cnt += 1
                    arr[nx][ny] = 0 #치즈 녹이기
    result.append(cnt)
    return cnt
t = 0
while True:
    t+=1
    cnt1 = bfs()
    if cnt1 == 0:
        break
print(t-1)
print(result[-2])

