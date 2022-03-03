import sys
import math
a,b,v = map(int,sys.stdin.readline().split())
day = 0
h = 0
while True:
    day += 1
    h += a
    if h == v:
        print(day)
        break
    h -= b
#아래는 시간초과 안남
day = (v-b)/(a-b)
print(math.ceil(day))