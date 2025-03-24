def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y
def solution(n, computers):
    global parent
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(i,j)
                print(parent)
    answer = set()
    for i in range(n):
        v = find(parent[i])
        answer.add(v)
    return len(answer)