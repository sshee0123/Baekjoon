def solution(my_string, is_prefix):
    answer = 0
    tmp = []
    for i in range(len(my_string)):
        tmp.append(my_string[:i])
    if is_prefix in tmp:
        answer = 1
    else:
        answer = 0
    return answer