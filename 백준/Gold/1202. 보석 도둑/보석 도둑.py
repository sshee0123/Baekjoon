import sys
import heapq
n, k = map(int,sys.stdin.readline().split())
q = [] # 보석 최소힙
bag = [] #가방 무게 리스트
for _ in range(n):
    heapq.heappush(q,list(map(int,sys.stdin.readline().split())))
for _ in range(k):
    bag.append(int(sys.stdin.readline()))
# 가방 오름차순 정렬
bag.sort()

result = 0
take = [] # 담은거
for c in bag:
    # 가방에 담을 수 있는 무게만 최대힙에 넣기
    while q and q[0][0] <= c:
        possible_m, possible_v = heapq.heappop(q)
        heapq.heappush(take, -possible_v)

    if take:
        result += (-heapq.heappop(take))

print(result)