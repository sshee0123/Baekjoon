import sys
input = sys.stdin.readline
# 재귀함수 호출 : 런타임 에러 (RecursionError)
sys.setrecursionlimit(10*6)

n = int(input())
m = int(input())
# 루트노드 리스트 초기화
parent = [i for i in range(n+1)]

# find 연산 : 루트 노드 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    # print(parent)
    return parent[x]

# union 연산 : 더 작은 루트노드로 합치기
def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        if arr[j] == 1: # i, j 연결되어 있으면 union 연산
            union(i,j)
# 계획
plan = list(map(int, input().split()))
result = "YES"
for i in range(1,m):
    if find(plan[i]-1) != find(plan[i-1]-1):
        result = "NO"
        break
print(result)
