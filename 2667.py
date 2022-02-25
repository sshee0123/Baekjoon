import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
result = 0
cnt_arr = []
def dfs(x,y):
    global cnt
    if 0<=x<n and 0<=y<n:
        if arr[x][y] == 1:
            cnt+=1
            arr[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True
    else:
        return False
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            cnt_arr.append(cnt)
            result += 1
            cnt = 0
cnt_arr.sort()
print(result)
for i in cnt_arr:
    print(i)
