import sys
input = sys.stdin.readline
# 재귀함수 호출 : 런타임 에러 (RecursionError)
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

# 루트노드 리스트 초기화
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i
# find 연산 : 루트 노드 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# union 연산 : 더 작은 루트노드로 합치기
def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(m):
    command, a, b = map(int, input().split())
    if command == 0: # 0이면 union 연산 수행
        union(a,b)
    else: # 1이면 a,b가 같은 루트 노드인지 확인
        if find(a) != find(b):
            print("NO")
        else:
            print("YES")