import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip())))
#bfs
dx = [0,-1,0,1]
dy = [1,0,-1,0]
#visited[0][0][0]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0,0,1))
#벽을 부술 수 있는 기회 1 줌.
visited[0][0][1] = 1
def bfs():
    while q:
        x,y,z = q.popleft()
        #종료지점에 도착한다면 출력
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                #벽이 없고 방문한 적 없다면
                if arr[nx][ny] == 0 and not visited[nx][ny][z]:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx,ny,z))
                #벽이 있고 벽을 뚫을 수 있다면
                elif arr[nx][ny] == 1 and z == 1:
                    visited[nx][ny][0] = visited[x][y][z] + 1
                    q.append((nx,ny,0))
    return -1
print(bfs())
