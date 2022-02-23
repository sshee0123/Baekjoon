import sys
t = int(sys.stdin.readline())
#스택
for i in range(t):
    string = sys.stdin.readline().rstrip()
    string += " "

    stack = []
    for j in string:
        if j != " ":
            stack.append(j)
        else:
            while stack:
                print(stack.pop(),end = "")
            print(' ',end="")
#문자열 슬라이싱
for i in range(t):
    string = sys.stdin.readline().rstrip().split()
    for str in string:
        print(str[::-1],end=" ")
    print()