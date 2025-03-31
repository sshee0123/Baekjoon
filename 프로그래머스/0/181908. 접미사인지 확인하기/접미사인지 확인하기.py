def solution(my_string, is_suffix):
    answer = 0
    str = []
    for i in range(len(my_string)):
        str.append(my_string[i:])
    if is_suffix in str:
        answer = 1
    else:
        answer = 0
    return answer