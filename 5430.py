import sys

t = int(sys.stdin.readline())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()[1:-2].rstrip().split(",")
    p = p.replace("RR","")

    rev = 0
    f,b = 0,0
    flag = 0 #error 인지 확인

    for j in p:
        if j=="R":
            rev+=1
        elif j== "D":
            if rev % 2 ==0:
                f+=1
            else:
                b+=1
    if f+b <= n:
        arr = arr[f:n-b]
        if rev % 2 ==0:
            print("["+",".join(arr)+"]")
        else:
            print("[" + ",".join(arr[::-1]) + "]")
    else:
        print("error")