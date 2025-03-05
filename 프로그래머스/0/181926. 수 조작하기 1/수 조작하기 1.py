def solution(n, control):
    answer = 0
    for c in control:
        if c == "w":
            n = n+1
        elif c == "s":
            n = n-1
        elif c == "d":
            n = n + 10
        elif c == "a":
            n = n-10
    return n
