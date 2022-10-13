import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
score = 0

def bfs(x, y, color):
    block_cnt, rainbow_cnt = 1, 0
    blocks, rainbows = [[x, y]], []
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and map[nx][ny] == color:
                visited[nx][ny] = 1
                block_cnt += 1
                blocks.append([nx, ny])
                q.append([nx, ny])
            elif 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and map[nx][ny] == 0:
                visited[nx][ny] = 1
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])
                q.append([nx, ny])

    for x, y in rainbows:
        visited[x][y] = 0
    return [block_cnt, rainbow_cnt, blocks + rainbows]


def remove(block):
    for x, y in block:
        map[x][y] = -2


def rotate(a):
    new_a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_a[n - j - 1][i] = a[i][j]
    return new_a


def gravity(a):
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if a[i][j] > -1:
                r = i
                while True:
                    if 0 <= r + 1 < n and a[r + 1][j] == -2:
                        a[r + 1][j] = a[r][j]
                        a[r][j] = -2
                        r += 1
                    else:
                        break

while True:
    visited = [[0] * n for _ in range(n)]
    blocks = []
    for i in range(n):
        for j in range(n):
            if map[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                block_info = bfs(i, j, map[i][j])
                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks.sort(reverse=True)
    if not blocks:
        break
    remove(blocks[0][2])
    score += blocks[0][0] ** 2
    gravity(map)
    map = rotate(map)
    gravity(map)

print(score)