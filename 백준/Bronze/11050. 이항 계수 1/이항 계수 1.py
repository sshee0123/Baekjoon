import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0]*(n+1) for _ in range(n+1)]

# 초기화
for i in range(n+1):
    dp[i][1] = i
    dp[i][0] = 1
    dp[i][i] = 1
# dp
for i in range(2,n+1):
    for j in range(i): # 고르는 수의 개수가 전체 개수를 넘을 수 없음
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        # dp[i][j] = dp[i][j] % 10007 # 모듈러연산
print(dp[n][k])