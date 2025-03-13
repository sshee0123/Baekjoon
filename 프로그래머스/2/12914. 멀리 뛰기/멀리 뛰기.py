def solution(n):
    if n == 1:
        return 1
    else:
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-2]+dp[i-1]
        return dp[-1]%1234567