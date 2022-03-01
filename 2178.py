import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip())))
#bfs
dx = [-1,0,1,0]
dy = [0,1,0,-1]
q = deque()
q.append((0,0))
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 1:
            arr[nx][ny] = arr[x][y] + 1
            q.append((nx,ny))
print(arr[n-1][m-1])

