def solution(n,a,b):
    answer = 0
    while a!=b:
        a,b = (a+1)//2, (b+1)//2
        answer += 1

    return answer