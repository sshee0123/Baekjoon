import sys
from itertools import combinations
n, s = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
#
# #백트래킹
# def dfs(idx,sum):
#     global cnt
#     if idx>=n:
#         return
#     sum += arr[idx]
#     if sum == s:
#         cnt+=1
#     dfs(idx+1, sum)
#     dfs(idx+1, sum-arr[idx])
#
# cnt = 0
# dfs(0,0)
# print(cnt)

#조합
cnt = 0
for i in range(1,n+1):
    comb = list(combinations(arr,i))
    for j in comb:
        if sum(j) == s:
            cnt+=1

print(cnt)