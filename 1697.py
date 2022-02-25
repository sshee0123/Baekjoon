import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())
MAX = 100000
visited = [0] * (MAX+1)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=MAX and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)
bfs()