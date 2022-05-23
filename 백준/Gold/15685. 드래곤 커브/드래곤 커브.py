import sys
n = int(sys.stdin.readline())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
graph = [[0]*101 for _ in range(101)]

for i in range(n):
    x, y, d, g = map(int,sys.stdin.readline().split())
    graph[x][y] = 1

    curv = [d]
    for ge in range(g):
        for c in range(len(curv)-1, -1, -1):
            curv.append((curv[c]+1) % 4)

    for i in range(len(curv)):
        x += dx[curv[i]]
        y += dy[curv[i]]
        if 0<=x<=100 and 0<=y<=100:
            graph[x][y]=1

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1]==1 and graph[i+1][j+1]==1:
            answer += 1
print(answer)