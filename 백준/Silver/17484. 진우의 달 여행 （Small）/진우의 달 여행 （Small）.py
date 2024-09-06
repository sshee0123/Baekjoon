import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dy = [-1, 0, 1]

# dfs(행, 열, 방향, 비교값, 정답)
def dfs(col, row, d, low, answer):
    if col == n-1: #달 도착
        return min(low, answer)
    for i in dy: #모든 방향 탐색
        if i != d: #두번 연속 같은 방향은 안됨
            if 0<=col<n and 0<=row+i<m: #이동 범위 체크
                low = dfs(col+1, row+i, i, low, answer + arr[col+1][row+i])
    return low

low = int(sys.maxsize)
for i in range(m):
    low = min(low, dfs(0, i, 2, low, arr[0][i]))
print(low)
