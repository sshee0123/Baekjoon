import sys
n = int(sys.stdin.readline())
d = [] #dp 테이블
for i in range(n):
    d.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n):
    for j in range(0,i+1):
        #각 줄의 맨 처음과 끝은 전 + 자기 자신
        if j == 0:
            d[i][j] = d[i-1][j] + d[i][j]
        elif j == i:
            d[i][j] = d[i-1][j-1] + d[i][j]
        else: #양 사이드 제외한 수들은 더 큰 것을 선택해서 자기자신 더함
            d[i][j] = max(d[i-1][j-1],d[i-1][j]) + d[i][j]
print(max(d[n-1]))