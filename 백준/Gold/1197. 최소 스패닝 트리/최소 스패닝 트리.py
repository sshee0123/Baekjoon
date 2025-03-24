import sys
input = sys.stdin.readline
from queue import PriorityQueue
sys.setrecursionlimit(1000000)
v, e = map(int, input().split())

pq = PriorityQueue() # 우선순위큐
# 루트노드 초기화
parent = [0] * (v+1)
for i in range(v+1):
    parent[i] = i

for i in range(e):
    a,b,c = map(int, input().split())
    pq.put((c,a,b)) # 가중치 우선으로 우선순위 큐에 삽입
# print(pq.queue) # 우선순위 큐 출력

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

useEdge = 0
result = 0
while useEdge < v-1:
    w,s,e = pq.get()
    # print(w,s,e)
    # 루트 노드가 같을 때까지 가중치 더하기
    if find(s) != find(e):
        union(s,e)
        useEdge += 1
        result += w
print(result)