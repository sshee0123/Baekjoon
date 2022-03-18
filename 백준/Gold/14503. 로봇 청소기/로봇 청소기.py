# 14503
import sys
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int,sys.stdin.readline().split())
r, c, d = map(int,sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

def rotate_left(d): # 현재 바라보고있는 방향에서 왼쪽으로
    return (d+3) % 4

def back(d): # 후진
    return (d+2) % 4

def bfs(r,c,d):
    q = deque()
    q.append([r, c, d])
    arr[r][c] = 2 # 청소
    cnt = 1
    while q:
        qr, qc, qd = q.popleft()
        tmp_qd = qd
        for i in range(4):
            tmp_qd = rotate_left(tmp_qd) # 현재 방향에서 왼쪽으로
            nr = qr + dx[tmp_qd]
            nc = qc + dy[tmp_qd]
            # 왼쪽에 청소안한 방이 있다면
            if 0<=nr<n and 0<=nc<m and arr[nr][nc] == 0:
                # 아직 청소 안했으면 청소하고 방향바꾸기
                arr[nr][nc] = 2
                cnt += 1
                q.append([nr,nc,tmp_qd])
                break

            # 갈 곳이 없다면
            elif i==3:
                # 방향 유지한채 한칸 후진
                nr = qr + dx[back(qd)]
                nc = qc + dy[back(qd)]
                q.append([nr, nc, qd])

                if arr[nr][nc] == 1: # 뒤에도 벽이 있다면 중단
                    return cnt

print(bfs(r,c,d))