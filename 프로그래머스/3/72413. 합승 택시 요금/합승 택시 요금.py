import sys
def solution(n, s, a, b, fares):
    answer = sys.maxsize
    # 거리 초기화
    d = [[sys.maxsize for i in range(n)] for j in range(n)]
    for i in range(n):
        d[i][i] = 0
    for cc,dd,f in fares:
        d[cc-1][dd-1] = f
        d[dd-1][cc-1] = f
        
    # 플로이드워셜 알고리즘 수행
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    
    # tmp 최단거리
    for t in range(n):
        tmp = d[s-1][t] + d[t][a-1] + d[t][b-1]
        answer = min(answer,tmp)
    return answer