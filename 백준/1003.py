import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    cnt0 = [1,0]
    cnt1 = [0,1]
    if n == 0:
        print(cnt0[0],cnt1[0])
    elif n ==1:
        print(cnt0[1], cnt1[1])
    else:
        for i in range(2,n+1):
            cnt0.append(cnt1[i-1])
            cnt1.append(cnt0[i-1] + cnt1[i-1])
        print(cnt0.pop(), cnt1.pop())
