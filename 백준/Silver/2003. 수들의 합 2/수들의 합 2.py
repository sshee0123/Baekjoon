# 2003
import sys
n, m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
cnt = 0
end = 0
tmp = 0
for start in range(n):
    while end < n and tmp < m:
        tmp += arr[end]
        end += 1
    if tmp == m:
        cnt += 1
    tmp -= arr[start]

print(cnt)