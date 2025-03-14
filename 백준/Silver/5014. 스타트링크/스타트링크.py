import sys
input = sys.stdin.readline
from collections import deque

f,s,g,u,d = map(int,input().split())
visited = [0]*(f+1)
def bfs():
    q = deque()
    q.append(s)
    visited[s] = 1 # 강호 방문
    while q:
        v = q.popleft()
        if v == g: # 강호가 있는 자리가 스타트링크면 이동 안한것이니 -1 하고 break
            print(visited[v]-1)
            break
        for cur in (v+u,v-d): # 강호자리에서 u만큼 올라가거나, d만큼 내려가거나
            if 0<cur<=f and not visited[cur]: # 가능한 이동거리는 1층부터 f층, 방문하지 않은 층
                visited[cur] = visited[v] + 1
                q.append(cur)
    if visited[g] == 0:
        print("use the stairs")
bfs()
