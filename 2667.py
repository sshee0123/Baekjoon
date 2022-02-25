import sys
from collections import deque

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
result = 0
cnt_arr = []
def dfs(x,y):
    global cnt
    if 0<=x<n and 0<=y<n:
        if arr[x][y] == 1:
            cnt+=1
            arr[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True
    else:
        return False

def bfs(graph,x,y):
    n = len(graph)
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    count = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx,ny))
                    count +=1
    return count
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt_arr.append(bfs(arr,i,j))

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            cnt_arr.append(cnt)
            result += 1
            cnt = 0
cnt_arr.sort()
print(result)
for i in cnt_arr:
    print(i)
