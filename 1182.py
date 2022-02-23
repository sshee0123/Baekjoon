import sys
n, s = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

def dfs(idx,sum):
    global cnt
    if idx>=n:
        return
    sum += arr[idx]
    if sum == s:
        cnt+=1
    dfs(idx+1, sum)
    dfs(idx+1, sum-arr[idx])

cnt = 0
dfs(0,0)
print(cnt)