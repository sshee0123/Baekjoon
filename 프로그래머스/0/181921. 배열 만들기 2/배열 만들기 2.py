def solution(l, r):
    answer = []
    for i in range(l,r+1):
        check = True # 0, 5로 이루어져있는지 체크
        for s in str(i):
            if s!='0' and s!='5':
                check = False
        if check: # 체크되어있으면 정답
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer