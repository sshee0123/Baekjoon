def solution(emergency):
    answer = []
    for i in emergency:
        cnt = 1
        for j in emergency:
            if i < j:
                cnt += 1
        answer.append(cnt)
    return answer