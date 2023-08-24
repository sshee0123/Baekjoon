from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((numbers[0], 0))
    q.append((-numbers[0],0))
    while q:
        num, cnt = q.popleft()
        cnt += 1
        if cnt <len(numbers):
            q.append((num+numbers[cnt],cnt))
            q.append((num-numbers[cnt],cnt))
        else:
            if num == target:
                answer += 1
    return answer