def solution(num_list):
    answer = 0
    tmp1, tmp2 = '',''
    for num in num_list:
        if num %2 != 0:
            tmp1 += str(num)
        else:
            tmp2 += str(num)
    answer = int(tmp1) + int(tmp2)
    return answer