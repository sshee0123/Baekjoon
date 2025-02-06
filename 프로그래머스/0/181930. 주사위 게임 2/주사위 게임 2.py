def solution(a, b, c):
    answer = 0
    check = len(set([a,b,c]))
    if check == 1:
        answer = (3*a) * (a**2*3) * (a**3*3)
    elif check == 2:
        answer = (a+b+c) * ((a**2)+(b**2)+(c**2))
    else:
        answer = (a+b+c)
    return answer