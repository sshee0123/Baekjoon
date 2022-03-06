import sys
import heapq
n = int(sys.stdin.readline())
left_heap = [] #최대힙
right_heap = [] #최소힙
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap,-num)
    else:
        heapq.heappush(right_heap,num)

    if len(left_heap)>=1 and len(right_heap)>=1 and -left_heap[0] > right_heap[0]:
        #중간값이 중간값이 아니면
        l_value = -heapq.heappop(left_heap)
        r_value = heapq.heappop(right_heap)

        heapq.heappush(left_heap,-r_value)
        heapq.heappush(right_heap,l_value)
    print(-left_heap[0])