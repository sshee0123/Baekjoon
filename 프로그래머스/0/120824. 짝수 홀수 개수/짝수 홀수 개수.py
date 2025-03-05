def solution(num_list):
    answer = []
    tmp1, tmp2 = 0, 0
    for n in num_list:
        if n%2 == 0:
            tmp1 += 1
        else:
            tmp2 += 1
    answer.append(tmp1)
    answer.append(tmp2)
    return answer