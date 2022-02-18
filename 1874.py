import sys
n = int(sys.stdin.readline())
stack = []
op = []
now = 1
possible = 1
for i in range(n):
    num = int(sys.stdin.readline())
    while now <= num:
        stack.append(now)
        op.append('+')
        now+=1

    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        possible = 0
if possible ==0:
    print("NO")
else:
    for i in op:
        print(i)


