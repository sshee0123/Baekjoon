import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
x = list(map(int, input().split()))
h = x[0]
if m == 1: #가로등이 한개면
    print(max(h, n-h))
else:
    for i in range(m):
        if i == m-1: #마지막 가로등
            tmp = n-x[-1]
        else:
            d = x[i+1]-x[i] #가로등 사이거리
            if d%2 == 0:
                tmp = d//2
            else:
                tmp = (d//2) + 1 #홀수는 2로 나눠도 모든 길을 비출수없어서
        h = max(h,tmp)
    print(h)
