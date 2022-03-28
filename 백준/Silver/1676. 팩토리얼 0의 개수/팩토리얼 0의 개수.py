#1676
import sys
import math
n = int(sys.stdin.readline())
fac = list(str(math.factorial(n)))
length = len(fac)-1
cnt = 0
while True:
    if fac[length] == '0':
        cnt += 1
        length -= 1
    else:
        break
print(cnt)