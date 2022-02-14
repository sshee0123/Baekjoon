import sys
T = int(sys.stdin.readline().strip())
for i in range(T):
    # s = list(sys.stdin.readline().strip())
    s = list(input())
    sum = 0
    for j in s:
        if j == "(":
            sum+=1
        elif j == ")":
            sum-=1
        if sum<0:
            print("NO")
            break
    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")
