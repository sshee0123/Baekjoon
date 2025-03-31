import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 원본배열
d = []
for i in range(n):
    d.append(list(map(int, input().split())))

# 누적합
d_sum = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        d_sum[i][j] = d_sum[i-1][j] + d_sum[i][j-1] - d_sum[i-1][j-1] + d[i-1][j-1]

# 정답 출력
for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    result = d_sum[x2][y2] - d_sum[x1-1][y2] - d_sum[x2][y1-1] + d_sum[x1-1][y1-1]
    print(result)