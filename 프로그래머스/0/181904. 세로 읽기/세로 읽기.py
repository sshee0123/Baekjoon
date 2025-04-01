def solution(my_string, m, c):
    answer = ''
    for i in range(0,len(my_string),m):
        tmp = my_string[i:i+m]
        answer += tmp[c-1]
    return answer