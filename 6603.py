import sys
from itertools import combinations

visited = [0] * 13
def dfs(start,depth):
    if depth == 6:
        for i in range(k):
            if visited[i]:
                print(s[i],end=" ")
        print()
        return
    for i in range(start,len(s)):
        visited[i] = 1
        dfs(i+1,depth+1)
        visited[i] = 0
    # if end == 6:
    #     for i in range(6):
    #         print(visited[i],end = " ")
    #     print()
    #     return
    # for i in range(start,len(s)):
    #     visited[end] = s[i]
    #     dfs(i+1, end+1)
while True:
    arr = list(map(int,sys.stdin.readline().split()))
    k = arr[0]
    if k == 0: #종료조건
        break
    s = arr[1:]
    #dfs
    dfs(0,0)
    print()
    #
    # #조합
    # n = list(combinations(s,6))
    # # print(n)
    # for i in n:
    #     for j in i:
    #         print(j,end=" ")
    #     print()
    # print()


