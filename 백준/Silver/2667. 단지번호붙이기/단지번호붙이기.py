import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip())))

dx = [1,-1,0,0]
dy = [0,0,-1,1]
cnt = 0 # 단지수
hcnt = 0 # 집 수
house = [] # 집 배열

def dfs(x,y):
    global hcnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1:
            graph[nx][ny] = 0 # 방문처리
            hcnt += 1 # 집 수 count
            dfs(nx,ny)

# 전체 탐색
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 1이면 집이 있어서 dfs 탐색
            hcnt += 1
            graph[i][j] = 0
            dfs(i,j)
            house.append(hcnt)
            hcnt = 0 # 집 수 초기화
            cnt += 1 # 단지 수 +1

# 각 단지내 집의 수 오름차순 정렬
house.sort()
print(cnt)
for h in house:
    print(h)
