# 11401
import sys
INF = int(1e9)
n = int(sys.stdin.readline()) # 도시 (노드)
m = int(sys.stdin.readline()) # 버스 (간선)
graph = [[INF]*(n+1) for _ in range(n+1)] # 최단경로 저장

# 자기 자신 지나는 경로 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
    # graph[a][b] = c
    graph[a][b] = min(graph[a][b],c)

# 플로이드 워셜 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 최단경로 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF: # 갈 수 없다면 0으로 출력
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()