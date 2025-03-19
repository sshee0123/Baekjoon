def solution(number):
    answer = sum(list(map(int,number)))%9
    return answer