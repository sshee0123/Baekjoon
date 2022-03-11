import sys
import heapq
n = int(sys.stdin.readline())
q = []
for _ in range(n):
    heapq.heappush(q,list(map(int,sys.stdin.readline().split())))
    # 최소힙에 삽입
target, fuel = map(int,sys.stdin.readline().split())

move = [] #움직인 큐 최대힙
cnt = 0
while fuel<target:
    while q and q[0][0]<=fuel:
        mf, pf = heapq.heappop(q)
        heapq.heappush(move,[-pf,mf])
        
    if not move:
        cnt = -1
        break
    pf1, mf1 = heapq.heappop(move)
    fuel += -pf1
    cnt += 1
print(cnt)