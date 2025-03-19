def solution(a, b, c, d):
    answer = 0
    tmp = [a,b,c,d]
    c = [tmp.count(x) for x in tmp]
    print(c)
    if max(c) == 4:
        answer = 1111*a
    elif max(c) == 3:
        answer = (10*tmp[c.index(3)]+tmp[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1: # 두 주사위는 같고 나머지 두 주사위 각각 다른경우
            answer = eval('*'.join([str(tmp[i]) for i,x in enumerate(c) if x == 1]))
        else:
            tmp1 = list(set(tmp))
            answer = (tmp1[0]+tmp1[1])*abs(tmp1[0]-tmp1[1])
    elif max(c) == 1:
        answer = min(tmp)
    return answer