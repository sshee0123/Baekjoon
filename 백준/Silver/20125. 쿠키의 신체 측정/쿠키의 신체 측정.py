
#머리
def cookieHead(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '*':
                return i,j
#왼쪽팔
def leftArm(x,y):
    cnt = 0
    for i in range(y-1, -1, -1):
        cnt += 1
        if arr[x][i] == '_':
            return cnt-1
    return cnt
#오른쪽팔
def rightArm(x,y):
    cnt = 0
    for i in range(y+1, n, 1):
        cnt += 1
        if arr[x][i] == '_':
            return cnt-1
    return cnt
#허리
def back(x,y):
    cnt = 0
    for i in range(x,n):
        cnt += 1
        if arr[i][y] == '_':
            break
    return cnt-1
#다리
def leg(x,y):
    cnt = 0
    for i in range(x,n):
        cnt += 1
        if arr[i][y] == '_':
            return cnt-1
    return cnt

import sys
n = int(input())
arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().strip()))
x, y = cookieHead(arr) #머리
print(x+2, y+1) #심장
# 왼쪽팔, 오른쪽팔, 허리, 왼쪽다리, 오른쪽다리
print(leftArm(x+1, y), end = " ")
print(rightArm(x+1, y), end = " ")
print(back(x+2, y), end = " ")
back = back(x+2, y)
print(leg(x+2+back, y-1), end = " ")
print(leg(x+2+back, y+1), end = " ")