def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        s,e = parts[i]
        my = my_strings[i]
        answer += my[s:e+1]
    return answer