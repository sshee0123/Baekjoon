N, M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))
answer = 0
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            answer+=1
            r,c = i,j
            if graph[i][j] == "-":
                while True:
                    visited[r][c] = 1
                    if c+1<M and graph[r][c] == graph[r][c+1]:
                        c+=1
                    else:
                        break
            else:
                while True:
                    visited[r][c] = 1
                    if r+1<N and graph[r][c] == graph[r+1][c]:
                        r+=1
                    else:
                        break
print(answer)
# for i in range(N):
#     pre = "|"
#     for j in range(M):
#         if graph[i][j] == "-":
#             if graph[i][j] != pre:
#                 answer += 1
#         pre = graph[i][j]
#
# for i in range(M):
#     pre = "-"
#     for j in range(N):
#         if graph[j][i] == "|":
#             if graph[j][i] != pre:
#                 answer += 1
#         pre = graph[j][i]
# print(answer)