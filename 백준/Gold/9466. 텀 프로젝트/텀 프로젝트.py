# 9466
import sys
sys.setrecursionlimit(111111)

def dfs(x):
    global result
    visited[x] = True
    cycled.append(x)

    if visited[s[x]]: # 방문했으면 싸이클 확인
        if s[x] in cycled:
            result += cycled[cycled.index(s[x]):]
        return
    else:
        dfs(s[x])

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s = [0] + list(map(int,sys.stdin.readline().split()))
    visited = [True] + [False] * n
    result = [] # 팀 구성한 학생 수

    for i in range(1,n+1):
        if not visited[i]:
            cycled = []
            dfs(i)

    print(n-len(result))
