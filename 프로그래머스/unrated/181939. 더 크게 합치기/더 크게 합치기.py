def solution(a, b):
    tmp = int(str(a)+str(b))
    tmp2 = int(str(b)+str(a))
    if tmp>=tmp2:
        return tmp
    else:
        return tmp2