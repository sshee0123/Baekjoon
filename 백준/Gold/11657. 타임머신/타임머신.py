import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
distance = [sys.maxsize] * (n+1)

# 에지 데이터 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))

#######벨만 포드 수행
# 시작 거리 0 초기화
distance[1] = 0
# 모든 에지 탐색
for _ in range(n-1):
    for s,e,d in edges:
        # 시작 노드 방문한적 없고 출발노드거리값 + 가중치 < 도착노드 거리값 일 때 거리값 업데이트
        if distance[s] != sys.maxsize and distance[s] + d < distance[e]:
            distance[e] = distance[s] + d

# 음수 사이클 판별 : 거리 업데이트 값 되면 음수사이클
minusCycle = False
for s,e,d in edges:
    if distance[s] != sys.maxsize and distance[s] + d < distance[e]:
        minusCycle = True
        break

if minusCycle == True:
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] == sys.maxsize:
            print(-1)
        else:
            print(distance[i])