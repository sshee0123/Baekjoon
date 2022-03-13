# 14502
import sys
from collections import deque
import copy

def bfs():
    q = deque()
    tmp_graph = copy.deepcopy(graph) # 벽 설치 그래프 깊은 복사
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2: # 바이러스 있는 좌표만 큐에 넣기
                q.append((i,j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                q.append((nx, ny))
    # 안전영역 ( 0인 칸 세기 )
    cnt0 = 0
    global answer
    for i in range(N):
        cnt0 += tmp_graph[i].count(0)
    answer = max(answer, cnt0)


def newwall(cnt):
    if cnt == 3:
        bfs() #벽 3개 새롭게 만들면 bfs 진행
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1 # 빈 칸이면 벽 설치
                newwall(cnt+1) # 벽 설치 재귀함수
                graph[i][j] = 0

N, M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
answer = 0
newwall(0) #벽 만들기
print(answer)

