import sys
import heapq
n = int(sys.stdin.readline())
q = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        #배열에서 가장 작은 값 출력 없으면 0
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        #배열에 x값 넣기
        heapq.heappush(q,x)

