def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        str = my_string[i:]
        answer.append(str)
    answer.sort()
    return answer