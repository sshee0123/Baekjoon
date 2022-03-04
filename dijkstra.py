import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split()) #간선, 노드
start = int(input()) #시작노드
#각 노드에 연결되어 있는 노드에 대한 정보 리스트
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))  #노드 a에서 노드 b로 가는 비용이 c라는 의미

#다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        #우선순위 큐에서 가장 최단 거리가 짧은 노드 꺼내기
        dist,node = heapq.heappop(q)
        #현재 노드가 이미 처리된 노드면 무시
        if distance[node] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[node]:
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

#모든 노드로 가는 최단거리 출력
for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])