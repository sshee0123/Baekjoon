import heapq as hq
def solution(n, costs):
    answer = 0
    
    graph = [[] for _ in range(n)]
    for a,b,w in costs:
        graph[a].append([w,b])
        graph[b].append([w,a])
    visited = [False]*n
    
    # 우선순위큐
    h = []
    hq.heappush(h,[0,0])
    cnt = 0
    while h and cnt<n: # 간선-1 만큼
        w,v = hq.heappop(h)
        if not visited[v]:
            visited[v] = True
            answer += w
            cnt += 1
            for i in graph[v]:
                hq.heappush(h,i)
    return answer