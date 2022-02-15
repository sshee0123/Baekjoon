import sys
n = int(input())
stack = []

for i in range(n):
    orders = sys.stdin.readline().split()

    if orders[0]=='push':
        stack.append(orders[1])
    elif orders[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif orders[0]=='size':
        print(len(stack))
    elif orders[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif orders[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])