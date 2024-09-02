import sys
N = int(input())
switches = [-1] + list(map(int, sys.stdin.readline().split()))
students = int(input())
def change(num):
    if switches[num] == 1:
        switches[num] = 0
    else:
        switches[num] = 1

for _ in range(students):
    s, k = map(int, input().split())
    if s == 1: #남자
        for i in range(k, N+1, k):
            change(i)
    elif s == 2: #여자
        change(k) #자기가 받은 수
        for i in range(N//2):
            if k-i<1 or k+i>N:
                break
            if switches[k-i] == switches[k+i]:
                change(k-i)
                change(k+i)
            else:
                break
#출력                
for i in range(1,N+1):
    print(switches[i], end=" ")
    if i % 20 == 0:
        print()