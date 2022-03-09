#7576
import sys
from collections import deque
m, n = map(int,sys.stdin.readline().split())
tomato = [[]*m for _ in range(n)]
for i in range(n):
    tomato[i] = list(map(int,sys.stdin.readline().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()
# 익은 토마토 좌표 큐에 넣기
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i,j))
def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append((nx,ny))

result = 0 #처음부터 모두 익은 상태
bfs()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0: #모두 익지 못함
            print(-1)
            sys.exit(0)
        result = max(result,tomato[i][j])
print(result-1) #처음에 익은 토마토부터 시작해서 1일 빼줘야함.