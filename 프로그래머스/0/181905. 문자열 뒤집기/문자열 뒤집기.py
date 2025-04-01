def solution(my_string, s, e):
    tmp = my_string[s:e+1]
    answer = my_string[:s] + tmp[::-1] + my_string[e+1:]
    return answer