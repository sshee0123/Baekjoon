#2527
import sys
for i in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int,sys.stdin.readline().split())
    # 직사각형이 겹치기 위한 계산
    # 왼쪽 변
    xl = max(x1, x3)
    # 오른쪽 변
    xr = min(x2, x4)
    # 윗 변
    upr = min(y2,y4)
    # 아랫 변
    downl = max(y1, y3)

    #겹치는 부분 (차이)
    diffx = xr-xl
    diffy = upr-downl

    # 차이가 둘다 양수면 겹치는 부분이 직사각형
    if diffx > 0 and diffy > 0:
        print("a")
    # 둘 다 0이면 점
    elif diffx == 0 and diffy == 0:
        print("c")
    # 공통부분이 없음
    elif diffx < 0 or diffy < 0:
        print("d")
    else: # 선분
        print("b")