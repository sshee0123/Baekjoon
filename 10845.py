import sys
from collections import deque
n = int(input())
q = deque()
for i in range(n):
    orders = sys.stdin.readline().split()

    if orders[0] == 'push':
        q.append(orders[1])
    elif orders[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif orders[0] == 'size':
        print(len(q))
    elif orders[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif orders[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif orders[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
