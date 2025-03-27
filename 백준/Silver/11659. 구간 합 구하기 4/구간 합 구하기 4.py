import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# 누적합
arr_sum = [0]*(n+1)
arr_sum[1] = arr[1]
for i in range(n+1):
    arr_sum[i] = arr_sum[i-1] + arr[i]

for _ in range(m):
    i,j = map(int, input().split())
    print(arr_sum[j]-arr_sum[i-1])