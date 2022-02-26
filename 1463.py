import sys
n = int(sys.stdin.readline())
#dp 테이블
d = [0]* (10**6+1)

for i in range(2,n+1):
    #1을 뺸다
    d[i] = d[i-1] + 1
    #3으로 나눠 떨어지면
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    #2으로 나눠 떨어지면
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

print(d[n])