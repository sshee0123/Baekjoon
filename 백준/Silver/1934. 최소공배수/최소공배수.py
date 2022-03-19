#1934
import sys
import math
t = int(sys.stdin.readline())
for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print(a*b//math.gcd(a,b))