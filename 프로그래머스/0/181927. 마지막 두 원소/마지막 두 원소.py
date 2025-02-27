def solution(num_list):
    tmp1 = num_list[-2:][0]
    tmp2 = num_list[-2:][1]
    print(tmp1,tmp2)
    if tmp2 > tmp1:
        num_list.append(tmp2-tmp1)
    else:
        num_list.append(tmp2*2)
    return num_list