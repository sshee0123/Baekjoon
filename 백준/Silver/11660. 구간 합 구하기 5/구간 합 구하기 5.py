import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[0] * (n+1)] # index가 1부터인 원본 배열
d = [[0] * (n+1) for _ in range(n+1)] # 합 배열

# 원본 배열 입력
for i in range(n):
    a_row = [0] + [int(x) for x in input().split()]
    a.append(a_row)

# 2차원 합 배열 생성
for x in range(1,n+1):
    for y in range(1,n+1):
        d[x][y] = d[x-1][y] + d[x][y-1] - d[x-1][y-1] + a[x][y]

# 정답 판 완성
for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    sum = d[x2][y2] - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1]
    print(sum)