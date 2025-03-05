import sys
input = sys.stdin.readline

n = int(input()) # 도시개수
m = int(input()) # 노선개수
distance = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]
for i in range(n+1):
    distance[i][i] = 0
for i in range(m):
    a,b,c = map(int, input().split())
    # 최단경로만
    if distance[a][b] > c:
        distance[a][b] = c

#플로이드워셜 알고리즘
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j] == sys.maxsize: # 갈수없으면 0
            print(0, end=" ")
        else:
            print(distance[i][j], end = " ")
    print()