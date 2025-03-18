from collections import deque
def solution(elements):
    answer = set()
    q = deque(elements)
    for i in range(len(q)):
        q.rotate(1)
        for j in range(1,len(q)):
            answer.add(sum(list(q)[:j]))
    return len(answer)+1