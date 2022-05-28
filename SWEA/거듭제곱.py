def myPow(N,M):
    global n,m,answer
    if M == m:
        answer = N
        return
    myPow(N*n, M+1)
     
for _ in range(10):
    t = int(input())
    n,m = map(int,input().split())
    myPow(n,1)
    print("#%d" %t, answer)
