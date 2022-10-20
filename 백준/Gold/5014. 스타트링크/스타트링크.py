from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        x = q.popleft()
        if x == G:
            return count[G]
        for i in (x+U, x-D):
            if 0<i<=F and not visited[i]:
                visited[i] = 1
                count[i] = count[x] + 1
                q.append(i)
    if count[G] == 0:
        return "use the stairs"
    
F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F+1)]
count = [0 for _ in range(F+1)]

print(bfs(S))