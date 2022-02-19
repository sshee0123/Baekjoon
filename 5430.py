import sys
from collections import deque
t = int(sys.stdin.readline())

for i in range(t):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()[1:-2].rstrip().split(",")

    if n ==0:
        q = deque()
    else:
        q = deque(arr)

    rev = 0
    flag = 0 #error 인지 확인

    for j in p:
        if j=="R":
            rev+=1
        elif j== "D":
            if len(q)==0:
                print("error")
                flag = 1
                break
            else:
                if rev % 2 ==0:
                    q.popleft()
                else:
                    q.pop()
    if flag == 0:
        if rev % 2 ==0:
            print("["+",".join(q)+"]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")