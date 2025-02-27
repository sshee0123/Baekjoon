def solution(num_list):
    answer = 0
    tmp = 1
    for num in num_list:
        tmp = tmp * num
    if tmp < sum(num_list)**2:
        return 1
    else:
        return 0