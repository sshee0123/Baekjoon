#2527
import sys
for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int,sys.stdin.readline().split())

    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        #겹치지 않음
        print("d")
        continue
    elif p1 == x2 or p2 == x1:
        if q1 == y2 or q2 == y1:
            print("c") #점
            continue
        else:
            print("b") #선분
            continue
    elif q1 == y2 or q2 == y1:
        print("b")
        continue
    else:
        print("a") #직사각형
        continue