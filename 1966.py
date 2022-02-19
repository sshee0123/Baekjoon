import sys
T = int(sys.stdin.readline())
for i in range(T):
    n,m = map(int,sys.stdin.readline().split())
    q = list(map(int,sys.stdin.readline().split()))
    check = [0 for _ in range(n)]
    check[m] = 1
    cnt = 0

    while True:
        if q[0] == max(q):
            cnt+=1
            if check[0] != 1:
                del q[0]
                del check[0]
            else:
                print(cnt)
                break
        else:
            q.append(q[0])
            check.append(check[0])
            del q[0]
            del check[0]