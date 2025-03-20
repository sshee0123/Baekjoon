def solution(want, number, discount):
    answer = 0
    check = True
    for i in range(len(discount)-9):
        tmp = discount[i:i+10]
        for w,n in zip(want,number):
            if w in tmp:
                n -= tmp.count(w)
            if n <=0:
                check = True
            else:
                check = False
                break
        if check:
            answer += 1

            
    return answer