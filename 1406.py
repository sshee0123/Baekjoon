import sys
s1 = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
s2 = []
for i in range(n):
    orders = sys.stdin.readline().split()
    if orders[0] == "L" and len(s1)!=0:
        s2.append(s1.pop())
    elif orders[0] == "D" and len(s2)!=0:
        s1.append(s2.pop())
    elif orders[0] == "B" and len(s1)!=0:
        s1.pop()
    elif orders[0] == "P":
        s1.append(orders[1])
print(''.join(s1+list(reversed(s2))))