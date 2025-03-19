def solution(a, b, c, d):
    answer = 0
    org = [a,b,c,d] # 원본 복사
    tmp = list(set([a,b,c,d])) # set to list
    n = len(tmp)
    if n == 1:
        answer = 1111*tmp[0]
    elif n == 2:
        for t in tmp:
            cnt = org.count(t)
            if cnt == 2: # 주사위가 두개씩 같은 값이 나온 경우
                answer = (tmp[0]+tmp[1])*abs(tmp[0]-tmp[1])
            elif cnt > 2: 
                cnt3 = [x for x in org if org.count(x)==3] # 세 주사위에서 나온 숫자
                cnt1 = [x for x in org if org.count(x)==1] # 나머지 다른 주사위에서 나온 숫자
                answer = (10*cnt3[0]+cnt1[0])**2
    elif n == 3:
        for t in tmp:
            cnt = org.count(t)
            if cnt == 2: 
                tmp1 = [x for x in org if x!=t] # 두 주사위에서 나온 숫자가 같은 경우 제외
                answer = tmp1[0]*tmp1[1]
    elif n == 4:
        answer = min(tmp)
    return answer