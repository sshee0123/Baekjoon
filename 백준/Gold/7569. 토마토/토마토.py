#7569
import sys
from collections import deque
m, n, h = map(int,sys.stdin.readline().split())
tomato = [[list(map(int,sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
# print(tomato)

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()
# 익은 토마토 좌표 큐에 넣기
for z in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[z][i][j] == 1:
                q.append((z,i,j))
def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                q.append((nz,nx,ny))

result = 0 #처음부터 모두 익은 상태
bfs()
for z in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[z][i][j] == 0: #모두 익지 못함
                print(-1)
                sys.exit(0) #종료
            result = max(result,tomato[z][i][j]) #모두 익는 날짜 or 0 중 가장 큰 것 답
print(result-1) #처음에 익은 토마토부터 시작해서 1일 빼줘야함.