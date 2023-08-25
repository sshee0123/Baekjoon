from collections import deque

def solution(maps):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    visited = [[-1]*m for _ in range(n)]
    
    q = deque()
    q.append((0,0)) # 처음에 1,1 위치
    visited[0][0] = 1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                if visited[nx][ny] == -1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] +1
        
    return visited[-1][-1]