# 14891
import sys
def rotate(gearnum, clockwise):
    isRotate = [False for _ in range(4)] # 각 톱니바퀴 회전 가능한지
    isDirection = [0 for _ in range(4)] # 각 톱니바퀴 방향
    isRotate[gearnum] = True
    isDirection[gearnum] = clockwise

    tempn = gearnum
    tempd = clockwise
    # gear[gearnum][6] 과 gearnum 전 톱니바퀴들의 [2]비교
    for i in range(gearnum-1,-1,-1):
        if gear[tempn][6] != gear[i][2]:
            # 다르면 반대방향으로 움직여야함
            tempd = -tempd # 새롭게 복사
            isDirection[i] = tempd
            tempn = i # 새롭게 복사
            isRotate[i] = True
        else: # 같으면 안움직여도됨
            break

    tempn = gearnum
    tempd = clockwise
    # gear[gearnum][2] 과 gearnum 후 톱니바퀴들의 [6]비교
    for i in range(gearnum+1, 4):
        if gear[tempn][2] != gear[i][6]:
            # 다르면 반대방향으로 움직여야함
            tempd = -tempd
            isDirection[i] = tempd
            tempn = i
            isRotate[i] = True
        else: # 같으면 안움직여도됨
            break

    # 톱니바퀴 회전
    for i in range(4):
        if isRotate[i]: # 회전 가능한 것만
            if isDirection[i] == 1: # 시계방향 회전
                # 마지막 pop해서 배열 처음에 붙이기
                tmp = gear[i].pop()
                gear[i] = [tmp] + gear[i]
            else: # 반시계방향 회전
                # 처음꺼 뽑아서 마지막에 붙이기
                tmp = gear[i][0]
                del gear[i][0]
                gear[i].append(tmp)

gear = []
for i in range(4):
    gear.append(list(sys.stdin.readline().rstrip()))
k = int(sys.stdin.readline()) #회전 횟수
for _ in range(k):
    # 톱니바퀴번호, 방향
    gear_num, clock_wise = map(int,sys.stdin.readline().split())
    rotate(gear_num-1, clock_wise)
result = 0
for i in range(4):
#     print(gear[i])
    if gear[i][0] == '1': # S극이면
        result += 2 ** i
print(result)