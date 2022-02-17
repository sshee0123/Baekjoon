import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque()
for i in range(n):
    orders = input().split()

    if orders[0] == 'push_front':
        q.appendleft(orders[1])
    elif orders[0] == 'push_back':
        q.append(orders[1])
    elif orders[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif orders[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
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
