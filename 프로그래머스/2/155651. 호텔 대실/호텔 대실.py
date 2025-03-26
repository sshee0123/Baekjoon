import heapq as hq

def solution(book_time):
    # hour to minute [start,end]
    book_minute = []
    for s,e in book_time:
        book_minute.append([int(s[:2])*60 + int(s[3:]) , int(e[:2])*60 + int(e[3:])])
    book_minute.sort()
    
    answer = 1 # 방 1개 초기값
    heap = [] # 우선순위 큐
    for s,e in book_minute:
        if not heap: # 비어있으면, 대실 종료시간 빠른 방 부터 push
            hq.heappush(heap, e+10)
            continue
            
        # 제일 먼저 들어간 방의 대실 종료 시간 <= 다음 예약된 대실 시작시간 
        if heap[0] <= s: 
            hq.heappop(heap)
        else:  # 아니면 방이 더 필요함
            answer += 1
        hq.heappush(heap,e+10)
    return answer