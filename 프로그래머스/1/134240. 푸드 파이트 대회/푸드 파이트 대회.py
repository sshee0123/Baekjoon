def solution(food):
    answer = ''
    tmp = ''
    for i in range(1,len(food)):
        f = food[i]//2
        tmp += str(i)*f
    answer = tmp+'0'
    answer += tmp[::-1]
    return answer