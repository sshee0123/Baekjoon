import sys
from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
def bfs(sx, sy, ex, ey):
    q = deque()
    q. append((sx, sy))
    chess[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            print(chess[x][y]-1)
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                q.append((nx,ny))



T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline()) #체스판 한 변
    sx, sy = map(int,sys.stdin.readline().split())
    ex, ey = map(int,sys.stdin.readline().split())
    #체스판 생성
    chess = [[0]*n for _ in range(n)]
    bfs(sx, sy, ex, ey)


