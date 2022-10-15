import sys
from collections import deque
n = int(sys.stdin.readline())
map = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
sx, sy, shark_w = 0, 0, 2
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(n):
        if map[i][j] == 9:
            sx, sy = i, j

def bfs(x, y, shark_weight):
    eat_temp = []
    q = deque()
    visited = [[0]*n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    q.append((x,y))
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if map[nx][ny] <= shark_weight: # 이동
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    distance[nx][ny] = distance[cx][cy] + 1
                # 먹을 물고기 있는 칸
                if map[nx][ny] < shark_weight and map[nx][ny]!=0:
                    eat_temp.append((nx,ny,distance[nx][ny]))
    return sorted(eat_temp,key=lambda x:(-x[2], -x[0], -x[1]))

time = 0
cnt = 0
while True:
    fishes = bfs(sx, sy, shark_w)
    if len(fishes)==0:
        break
    fx, fy, fd = fishes.pop()
    time += fd
    map[fx][fy] , map[sx][sy] = 0, 0 # 물고기 먹은 칸, 상어칸 다시 빈칸으로
    sx, sy = fx, fy
    cnt += 1
    if cnt == shark_w:
        shark_w += 1
        cnt=0
print(time)
