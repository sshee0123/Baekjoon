import sys
from collections import deque
m, n, k = map(int,sys.stdin.readline().split())
arr = [[0]*n for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#직사각형 k개 1로 표시
for i in range(k):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            arr[y][x] = 1
# print(arr)

#bfs
result = []

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0: #갈 수 있는 길이면
            cnt = 1
            arr[i][j] = 1
            #bfs
            q = deque()
            q.append((i,j))
            while q:
                y,x = q.popleft()
                for c in range(4):
                    ny = y+ dy[c]
                    nx = x+ dx[c]
                    if 0<=ny<m and 0<=nx<n and arr[ny][nx] == 0:
                        cnt += 1
                        arr[ny][nx] = 1
                        q.append((ny,nx))
            result.append(cnt)
print(len(result))
result.sort()
for i in result:
    print(i,end=" ")