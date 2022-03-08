#2156
import sys
n = int(sys.stdin.readline())
arr = [0]*10000 #포도주
for i in range(n):
    arr[i] = int(sys.stdin.readline())

#dp테이블
#dp[i] = 0부터 i번째 포도주까지 최대로 마신 양
dp = [0] * 10000
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2], dp[1])

for i in range(3,n):
    dp[i] = max(dp[i-2]+arr[i], arr[i-1]+arr[i]+dp[i-3], dp[i-1])
print(max(dp))