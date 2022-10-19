from collections import deque
def distance(x1,x2,y1,y2):
    return abs(x1-x2) + abs(y1-y2)
def bfs():
    q = deque()
    q.append((sx,sy))
    while q:
        x, y = q.popleft()
        # 처음에 맥주 한박스 들고 시작함
        if distance(x,ex,y,ey) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = cu[i] # 편의점에서 맥주 받기
                if distance(nx,x,ny,y) <= 1000:
                    q.append((nx,ny))
                    visited[i] = 1
    print("sad")
    return
t = int(input())
for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    cu = []
    for i in range(n):
        x, y = map(int, input().split())
        cu.append([x,y])
    ex, ey = map(int, input().split())
    visited = [0]*(n+1)
    bfs()