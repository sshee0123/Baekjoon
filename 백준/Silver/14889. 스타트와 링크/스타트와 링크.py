# 14889
import sys
from itertools import combinations
n = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

members = [i for i in range(n)]
cases = list(combinations(members,n//2)) # 팀 나누는 경우의 수
min_v = 1e9
for case in cases:
    c2 = list(set(members)-set(case))
    start, link = 0,0
    for i in range(n//2):
        for j in range(i+1, n//2):
            start += arr[case[i]][case[j]] + arr[case[j]][case[i]]
            link += arr[c2[i]][c2[j]] + arr[c2[j]][c2[i]]
    min_v = min(min_v, abs(start-link))
print(min_v)